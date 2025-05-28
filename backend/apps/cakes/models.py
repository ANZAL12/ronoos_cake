from django.db import models
from django.conf import settings

class Cake(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    baker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cakes')
    image = models.ImageField(upload_to='cakes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
