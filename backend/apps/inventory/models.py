from django.db import models
from django.db import models
from backend.apps.cakes.models import Cake


class Inventory(models.Model):
    cake = models.OneToOneField(Cake, on_delete=models.CASCADE)  # Link to the Cake model
    stock_quantity = models.PositiveIntegerField(default=0)  # Number of cakes available in stock
    reorder_level = models.PositiveIntegerField(default=5)  # Minimum stock before restocking is triggered
    last_updated = models.DateTimeField(auto_now=True)  # Automatically updated on changes

    def __str__(self):
        return f"{self.cake.name} - Stock: {self.stock_quantity}"

    def is_restock_needed(self):
        """Check if the stock is below the reorder level."""
        return self.stock_quantity <= self.reorder_level
