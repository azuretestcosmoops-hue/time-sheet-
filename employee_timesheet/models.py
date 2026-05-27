from django.db import models
from django.contrib.auth.models import User


class Timesheet(models.Model):

    TEAM_CHOICES = [
        ("HR", "HR"),
        ("SALES", "Sales"),
        ("IT_ADMIN", "IT Admin"),
        ("CFO", "CFO"),
        ("PRACTICE_HEAD", "Practice Head"),
        ("PRINCIPAL_ENGINEER", "Principal Software Engineer"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    team = models.CharField(
        max_length=50,
        choices=TEAM_CHOICES,
        default="HR"
    )

    date = models.DateField(auto_now_add=True)
    task = models.CharField(max_length=255)

    start_time = models.TimeField(null=True, blank=True)

    hours = models.FloatField(default=0)

    comments = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.team} - {self.task} - {self.date}"
        return f"Unknown User - {self.task} - {self.date}"
