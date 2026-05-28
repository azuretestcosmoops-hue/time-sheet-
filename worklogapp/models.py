from django.db import models
from django.contrib.auth.models import User


# Employee Profile Model
class EmployeeProfile(models.Model):

    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('PracticeHead', 'PracticeHead'),
        ('PrincipalSoftwareEngineer', 'PrincipalSoftwareEngineer'),
        ('HR', 'HR'),
        ('Sales', 'Sales'),
        ('CFO', 'CFO'),
        ('Employee', 'Employee'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=100,
        choices=ROLE_CHOICES,
        default='Employee'
    )

    reporting_manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )

    def __str__(self):
        return self.user.username


# Timesheet / Task Model
class TimeSheet(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='worklog_timesheets'
    )

    title = models.CharField(
        max_length=200
    )

    date = models.DateField()

    hours = models.FloatField()

    description = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_tasks'
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.title}"
