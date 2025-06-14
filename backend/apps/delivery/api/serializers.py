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
        extra_kwargs = {
            'location': {'required': True},
            'address': {'required': True}
        }

    def validate(self, data):
        # Get the user from the request
        user = self.context['request'].user
        
        # If customer_name is not provided or empty, use user's full name
        if not data.get('customer_name'):
            data['customer_name'] = f"{user.first_name} {user.last_name}".strip() or user.username
        
        # If mobile_number is not provided or empty, use user's mobile number
        if not data.get('mobile_number') and hasattr(user, 'profile'):
            data['mobile_number'] = user.profile.mobile_number
        
        return data

    def create(self, validated_data):
        # Get the user from the request
        user = self.context['request'].user
        
        # If customer_name is not set, use user's full name
        if not validated_data.get('customer_name'):
            validated_data['customer_name'] = f"{user.first_name} {user.last_name}".strip() or user.username
        
        # If mobile_number is not set, use user's mobile number
        if not validated_data.get('mobile_number') and hasattr(user, 'profile'):
            validated_data['mobile_number'] = user.profile.mobile_number
        
        return super().create(validated_data)
