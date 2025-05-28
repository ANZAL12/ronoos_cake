from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from backend.apps.cakes.models import Cake
from backend.apps.users.models import User
from backend.apps.users.api.serializers import UserSerializer
from .serializers import CakeSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

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

class CakeListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        cakes = Cake.objects.all()
        serializer = CakeSerializer(cakes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CakeSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure we're using the authenticated user
            if not request.user.is_authenticated:
                return Response(
                    {"detail": "Authentication credentials were not provided."},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            serializer.save(baker=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CakeDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_object(self, pk):
        try:
            return Cake.objects.get(pk=pk)
        except Cake.DoesNotExist:
            return None

    def get(self, request, pk):
        cake = self.get_object(pk)
        if not cake:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CakeSerializer(cake)
        return Response(serializer.data)

    def put(self, request, pk):
        cake = self.get_object(pk)
        if not cake:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Only allow the baker to update their own cake
        if cake.baker != request.user:
            return Response(
                {"detail": "You don't have permission to update this cake."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = CakeSerializer(cake, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cake = self.get_object(pk)
        if not cake:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Only allow the baker to delete their own cake
        if cake.baker != request.user:
            return Response(
                {"detail": "You don't have permission to delete this cake."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        cake.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BakerCakeListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cakes = Cake.objects.filter(baker=request.user)
        serializer = CakeSerializer(cakes, many=True)
        return Response(serializer.data)
