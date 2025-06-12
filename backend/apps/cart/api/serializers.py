from rest_framework import serializers
from backend.apps.users.models import User
from backend.apps.cart.models import Cart, CartItem
from backend.apps.cakes.models import Cake


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

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ['id', 'name', 'price', 'offer_price', 'image', 'description']

class CartItemSerializer(serializers.ModelSerializer):
    cake = CakeSerializer(read_only=True)
    cake_id = serializers.PrimaryKeyRelatedField(queryset=Cake.objects.all(), source='cake', write_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'cake', 'cake_id', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items', 'total_price']
