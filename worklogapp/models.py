from django.db import models
from django.contrib.auth.models import User


class TimeSheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    hours = models.FloatField()
    description = models.TextField(blank=True, null=True)

    # ✅ FIX HERE
    created_at = models.DateTimeField(auto_now_add=True)
