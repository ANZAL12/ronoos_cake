from rest_framework import serializers
from backend.apps.users.models import User
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_baker', 'is_customer', 'is_staff', 'password', 'mobile_number']
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

    def validate_mobile_number(self, value):
        if not value:
            raise serializers.ValidationError('Mobile number is required.')
        if not re.match(r'^\d{10,15}$', value):
            raise serializers.ValidationError('Mobile number must be 10-15 digits.')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_baker=validated_data.get('is_baker', False),
            is_customer=validated_data.get('is_customer', False),
            is_staff=validated_data.get('is_staff', False),
            mobile_number=validated_data.get('mobile_number', '')
        )
        return user
