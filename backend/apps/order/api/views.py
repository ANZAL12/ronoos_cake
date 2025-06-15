from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.apps.users.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from backend.apps.order.models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import action
import logging

logger = logging.getLogger(__name__)

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

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        logger.info(f"Getting orders for user: {user.username}, is_baker: {getattr(user, 'is_baker', False)}")
        if getattr(user, 'is_baker', False):
            # Bakers can see all orders
            return Order.objects.all()
        # Regular customers can only see their own orders
        return Order.objects.filter(customer=user)

    def create(self, request, *args, **kwargs):
        logger.info(f"Creating order with data: {request.data}")
        # Add request to serializer context
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            logger.error(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            self.perform_create(serializer)
            logger.info(f"Order created successfully: {serializer.data}")
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            logger.error(f"Error creating order: {str(e)}")
            return Response(
                {"detail": f"Error creating order: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def list(self, request, *args, **kwargs):
        logger.info(f"Listing orders for user: {request.user.username}")
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        logger.info(f"Found {len(serializer.data)} orders")
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # Check if this is a delete-all request
        if kwargs.get('pk') == 'delete-all':
            # Only allow admin or baker to delete all orders
            if not (getattr(request.user, 'is_baker', False) or getattr(request.user, 'is_admin', False)):
                return Response(
                    {"detail": "You don't have permission to delete all orders."},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            try:
                # Delete all orders
                Order.objects.all().delete()
                return Response(
                    {"detail": "All orders have been deleted successfully."},
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {"detail": f"Error deleting orders: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        # Handle single order deletion
        return super().destroy(request, *args, **kwargs)

    def update_status(self, request, pk=None):
        logger.info(f"Updating status for order {pk}")
        try:
            order = self.get_object()
            new_status = request.data.get('status')
            logger.info(f"New status: {new_status}")
            
            if new_status not in dict(Order.STATUS_CHOICES):
                logger.error(f"Invalid status: {new_status}")
                return Response(
                    {'detail': 'Invalid status.'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            order.status = new_status
            order.save()
            logger.info(f"Status updated successfully for order {pk}")
            return Response({'id': order.id, 'status': order.status})
        except Order.DoesNotExist:
            logger.error(f"Order {pk} not found")
            return Response(
                {'detail': 'Order not found.'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f"Error updating status: {str(e)}")
            return Response(
                {'detail': f'Error updating status: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['get'], url_path='all-details')
    def all_details(self, request):
        user = request.user
        if not getattr(user, 'is_baker', False):
            return Response({'detail': 'Only bakers can access all order details.'}, status=status.HTTP_403_FORBIDDEN)
        orders = Order.objects.all().order_by('-created_at')
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)
