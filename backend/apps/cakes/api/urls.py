from django.urls import path
from .views import (
    CakeListCreateAPIView,
    CakeDetailAPIView,
    BakerCakeListAPIView,
    ActiveCakeListAPIView
)

app_name = 'cakes'

urlpatterns = [
    # Cake endpoints
    path('cakes/', CakeListCreateAPIView.as_view(), name='cake-list-create'),
    path('cakes/<int:pk>/', CakeDetailAPIView.as_view(), name='cake-detail'),
    path('baker/cakes/', BakerCakeListAPIView.as_view(), name='baker-cake-list'),
    path('cakes/active/', ActiveCakeListAPIView.as_view(), name='cake-active-list'),
]
