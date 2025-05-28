from django.db import models
from backend.apps.order.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)  # Associated order
    payment_method = models.CharField(max_length=50)  # e.g., Credit Card, UPI, Cash
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Amount paid
    payment_date = models.DateTimeField(auto_now_add=True)  # Payment timestamp
    status = models.CharField(max_length=50, default='Pending')  # e.g., Completed, Pending

    def __str__(self):
        return f"Payment for Order {self.order.id}"
