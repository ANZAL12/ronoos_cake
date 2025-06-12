from rest_framework import serializers
from backend.apps.users.models import User
from backend.apps.cakes.models import Cake
from backend.apps.users.api.serializers import UserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CakeSerializer(serializers.ModelSerializer):
    baker = UserSerializer(read_only=True)
    
    class Meta:
        model = Cake
        fields = ['id', 'name', 'description', 'price', 'offer_price', 'baker', 'image', 
                 'is_available', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
