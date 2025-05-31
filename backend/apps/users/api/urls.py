from django.urls import path
from .views import UserListCreateAPIView, UserDetailAPIView, LoginView, BakerLoginView, CustomerLoginView, StaffLoginView

app_name = 'users'

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('login/baker/', BakerLoginView.as_view(), name='login-baker'),
    path('login/customer/', CustomerLoginView.as_view(), name='login-customer'),
    path('login/staff/', StaffLoginView.as_view(), name='login-staff'),
]