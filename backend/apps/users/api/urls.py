from django.urls import path
from .views import UserListCreateAPIView, UserDetailAPIView, LoginView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='user-login'),
]