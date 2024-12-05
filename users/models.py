from django.db import models
from django.contrib.auth.models import User

# Model to store health metrics data
class HealthMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_health_metrics")
    health_data = models.JSONField()
    blood_pressure = models.CharField(max_length=100)
    glucose_level = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Health data for {self.user.username} at {self.timestamp}"
class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_token = models.CharField(max_length=255, unique=True)
    last_active = models.DateTimeField(auto_now=True)

