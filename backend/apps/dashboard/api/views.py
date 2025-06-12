from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.apps.users.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from backend.apps.order.models import Order
from backend.apps.review.models import Review
from backend.apps.payment.models import Payment
from message.models import Message
from backend.apps.cakes.models import Cake

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

class RecentActivityAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        activities = []

        for order in Order.objects.order_by('-created_at')[:5]:
            activities.append({
                "id": f"order-{order.id}",
                "type": "order",
                "icon": "shopping-cart",
                "title": "New Order Received",
                "description": f"{order.cake} - {order.customer}",
                "time": order.created_at,
            })

        for review in Review.objects.order_by('-created_at')[:5]:
            activities.append({
                "id": f"review-{review.id}",
                "type": "review",
                "icon": "star",
                "title": "New Review",
                "description": f"{'⭐' * int(review.rating)} \"{review.comment[:40]}{'...' if len(review.comment) > 40 else ''}\"",
                "time": review.created_at,
            })

        for payment in Payment.objects.order_by('-payment_date')[:5]:
            activities.append({
                "id": f"payment-{payment.id}",
                "type": "payment",
                "icon": "credit-card",
                "title": "Payment Received",
                "description": f"{payment.amount_paid} for {payment.order}",
                "time": payment.payment_date,
            })

        for msg in Message.objects.order_by('-created_at')[:5]:
            activities.append({
                "id": f"msg-{msg.id}",
                "type": "message",
                "icon": "mail",
                "title": "New Message",
                "description": f"From {msg.name}: \"{msg.message[:40]}{'...' if len(msg.message) > 40 else ''}\"",
                "time": msg.created_at,
            })

        for cake in Cake.objects.order_by('-created_at')[:5]:
            activities.append({
                "id": f"cake-{cake.id}",
                "type": "cake",
                "icon": "plus-circle",
                "title": "Cake Added",
                "description": f"{cake.name} added to menu",
                "time": cake.created_at,
            })

        activities.sort(key=lambda x: x['time'], reverse=True)
        for act in activities:
            act['time'] = act['time'].isoformat()
        return Response(activities[:15])
