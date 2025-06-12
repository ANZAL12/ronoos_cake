from rest_framework import generics, permissions
from backend.apps.message.models import Message
from .serializers import MessageSerializer

class MessageCreateAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

class MessageListAPIView(generics.ListAPIView):
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only bakers/admins should see
