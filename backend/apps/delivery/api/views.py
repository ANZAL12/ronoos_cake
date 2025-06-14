from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.apps.users.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from backend.apps.delivery.models import Delivery
from .serializers import DeliverySerializer
from backend.apps.order.models import Order

class UserListCreateAPIView(APIView):
    def get(self, request):
        is_baker = request.query_params.get('is_baker')  # Check if filtering by baker is requested
        if is_baker:
            users = User.objects.filter(profile__is_baker=True)  # Adjust filter as per your model
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_staff': user.is_staff
            }
        })

class DeliveryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DeliverySerializer

    def get_queryset(self):
        return Delivery.objects.filter(order__customer=self.request.user)

    def create(self, request, *args, **kwargs):
        # Check if delivery details already exist for this order
        order_id = request.data.get('order')
        if not order_id:
            return Response(
                {'detail': 'Order ID is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verify that the order exists and belongs to the user
        try:
            order = Order.objects.get(id=order_id, customer=request.user)
        except Order.DoesNotExist:
            return Response(
                {'detail': f'Order with ID {order_id} does not exist or does not belong to you'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if Delivery.objects.filter(order_id=order_id).exists():
            return Response(
                {'detail': 'Delivery details already exist for this order'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Auto-populate customer details from user profile
        data = request.data.copy()
        user = request.user
        
        # Only set customer_name if not provided or empty
        if not data.get('customer_name'):
            data['customer_name'] = f"{user.first_name} {user.last_name}".strip() or user.username
        
        # Only set mobile_number if not provided or empty
        if not data.get('mobile_number') and hasattr(user, 'profile'):
            data['mobile_number'] = user.profile.mobile_number
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
