from rest_framework import serializers
from backend.apps.users.models import User
from backend.apps.delivery.models import Delivery


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_baker', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_baker=validated_data.get('is_baker', False)
        )
        return user


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'order', 'customer_name', 'mobile_number', 'location', 'address', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
