from rest_framework import serializers
from backend.apps.users.models import User
from backend.apps.order.models import Order, OrderItem
from backend.apps.cakes.models import Cake
from decimal import Decimal
from backend.apps.delivery.models import Delivery
from backend.apps.delivery.api.serializers import DeliverySerializer
import logging

logger = logging.getLogger(__name__)

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

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'mobile_number']

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
    customer = UserPublicSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(is_customer=True),
        write_only=True,
        required=False
    )
    customer_name = serializers.CharField(write_only=True, required=False)
    mobile_number = serializers.CharField(write_only=True, required=False)
    location = serializers.CharField(write_only=True, required=False)
    delivery = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'customer_id', 'customer_name', 'mobile_number', 'location', 
                 'total_amount', 'status', 'created_at', 'items', 'delivery']
        read_only_fields = ['total_amount', 'status', 'created_at', 'customer', 'delivery']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Include manual customer details in the response
        if not instance.customer:
            data['customer_name'] = instance.customer_name
            data['mobile_number'] = instance.mobile_number
            data['location'] = instance.location
        return data

    def get_delivery(self, obj):
        try:
            delivery = obj.delivery
            return DeliverySerializer(delivery).data
        except Delivery.DoesNotExist:
            return None

    def create(self, validated_data):
        logger.info(f"Creating order with validated data: {validated_data}")
        items_data = validated_data.pop('items')
        customer = validated_data.pop('customer_id', None)
        customer_name = validated_data.pop('customer_name', None)
        mobile_number = validated_data.pop('mobile_number', None)
        location = validated_data.pop('location', None)
        request_user = self.context['request'].user

        logger.info(f"Processing order for user: {request_user.username}, is_baker: {getattr(request_user, 'is_baker', False)}")
        logger.info(f"Customer data - id: {customer}, name: {customer_name}, mobile: {mobile_number}, location: {location}")

        # Create order with either existing customer or manual details
        if customer and getattr(request_user, 'is_baker', False):
            logger.info(f"Creating order for existing customer: {customer}")
            order_customer = customer
            order = Order.objects.create(
                customer=order_customer,
                status='pending',
                total_amount=Decimal('0.00')
            )
        else:
            # For manual orders, validate required fields
            if not all([customer_name, mobile_number, location]):
                logger.error("Missing required fields for manual order")
                raise serializers.ValidationError(
                    "For manual orders, customer_name, mobile_number, and location are required"
                )
            logger.info(f"Creating manual order for: {customer_name}")
            order = Order.objects.create(
                customer_name=customer_name,
                mobile_number=mobile_number,
                location=location,
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
        logger.info(f"Order created successfully with total amount: {total_amount}")
        return order
