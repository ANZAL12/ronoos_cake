from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.apps.users.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes

class UserListCreateAPIView(APIView):
    permission_classes = [AllowAny]  # Allow registration without authentication

    def get(self, request):
        is_baker = request.query_params.get('is_baker')  # Check if filtering by baker is requested
        if is_baker:
            users = User.objects.filter(is_baker=True)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Don't pop password, let serializer handle it
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
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
                'is_baker': user.is_baker,
                'is_staff': user.is_staff,
                'is_customer': user.is_customer
            }
        })

class BakerLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None or not getattr(user, 'is_baker', False):
            return Response({'error': 'Invalid credentials or not a baker'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_baker': user.is_baker,
                'is_staff': user.is_staff,
                'is_customer': user.is_customer
            }
        })

class CustomerLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None or not getattr(user, 'is_customer', False):
            return Response({'error': 'Invalid credentials or not a customer'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_baker': user.is_baker,
                'is_staff': user.is_staff,
                'is_customer': user.is_customer
            }
        })

class StaffLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None or not getattr(user, 'is_staff', False):
            return Response({'error': 'Invalid credentials or not staff'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_baker': user.is_baker,
                'is_staff': user.is_staff,
                'is_customer': user.is_customer
            }
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_search(request):
    query = request.GET.get('q', '')
    if query:
        customers = User.objects.filter(is_customer=True, username__icontains=query)
    else:
        customers = User.objects.filter(is_customer=True)
    serializer = UserSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_list(request):
    customers = User.objects.filter(is_customer=True)
    serializer = UserSerializer(customers, many=True)
    return Response(serializer.data)
