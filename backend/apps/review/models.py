from django.db import models
from backend.apps.cakes.models import Cake
from backend.apps.users.models import User


class Review(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)  # Associated cake
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Customer leaving the review
    rating = models.PositiveSmallIntegerField()  # Rating (e.g., 1 to 5 stars)
    comment = models.TextField(blank=True)  # Review text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"Review by {self.customer.username} for {self.cake.name}"

