from django.db import models
from backend.apps.order.models import Order

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.TextField()  # Delivery address
    delivery_date = models.DateTimeField()  # Scheduled delivery time
    status = models.CharField(max_length=50, default='Pending')  # e.g., Pending, Delivered

    def __str__(self):
        return f"Delivery for Order {self.order.id}"

