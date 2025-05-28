from django.db import models
from backend.apps.users.models import User

class Notification(models.Model):
    baker = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_baker': True})  
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for Baker {self.baker.username}"

