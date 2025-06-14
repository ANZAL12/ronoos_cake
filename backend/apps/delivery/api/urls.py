from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserListCreateAPIView, UserDetailAPIView, LoginView, DeliveryViewSet

router = DefaultRouter()
router.register(r'', DeliveryViewSet, basename='delivery')

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    path('', include(router.urls)),
]