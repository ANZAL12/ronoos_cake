from django.db import models
from django.conf import settings
from backend.apps.order.models import Order

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery')
    customer_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    location = models.CharField(max_length=200, help_text="Location coordinates or landmark")
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery for Order #{self.order.id} - {self.customer_name}"

