from rest_framework import serializers
from backend.apps.users.models import User
from backend.apps.order.models import Order, OrderItem
from backend.apps.cakes.models import Cake
from decimal import Decimal


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

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['cake', 'quantity', 'price']
        read_only_fields = ['price']

    def validate_cake(self, value):
        if not value.is_available:
            raise serializers.ValidationError("This cake is not available")
        return value

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return value

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'total_amount', 'status', 'created_at', 'items']
        read_only_fields = ['total_amount', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(
            customer=self.context['request'].user,
            status='pending',
            total_amount=Decimal('0.00')
        )

        total_amount = Decimal('0.00')
        for item_data in items_data:
            cake = item_data['cake']
            quantity = item_data['quantity']
            price = Decimal(str(cake.price)) * Decimal(str(quantity))
            total_amount += price
            
            OrderItem.objects.create(
                order=order,
                cake=cake,
                quantity=quantity,
                price=price
            )

        order.total_amount = total_amount
        order.save()
        return order
