from django.contrib import admin
from .models import TimeSheet, EmployeeProfile


@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'title',
        'date',
        'hours',
        'status',
    )


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'role',
        'reporting_manager',
    )
