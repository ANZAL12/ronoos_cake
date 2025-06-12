from django.urls import path
from .views import MessageCreateAPIView, MessageListAPIView

urlpatterns = [
    path('', MessageCreateAPIView.as_view(), name='message-create'),
    path('list/', MessageListAPIView.as_view(), name='message-list'),
]
