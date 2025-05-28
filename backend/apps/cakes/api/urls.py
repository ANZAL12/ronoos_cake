from django.urls import path
from .views import (
    CakeListCreateAPIView,
    CakeDetailAPIView,
    BakerCakeListAPIView,
    UserListCreateAPIView,
    UserDetailAPIView,
    LoginView
)

app_name = 'cakes'

urlpatterns = [
    # Cake endpoints
    path('cakes/', CakeListCreateAPIView.as_view(), name='cake-list-create'),
    path('cakes/<int:pk>/', CakeDetailAPIView.as_view(), name='cake-detail'),
    path('baker/cakes/', BakerCakeListAPIView.as_view(), name='baker-cake-list'),
    
    # User endpoints
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
]
