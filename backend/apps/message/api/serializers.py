from rest_framework import serializers
from backend.apps.message.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'name', 'email', 'message', 'created_at']
