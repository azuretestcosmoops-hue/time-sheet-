from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TimeSheet, EmployeeProfile


@login_required
def home(request):

    user = request.user

    # 🔥 ADMIN
    if user.is_superuser:
        tasks = TimeSheet.objects.all().order_by("-id")
        role = "admin"

    else:
        try:
            profile = EmployeeProfile.objects.get(user=user)
            role = profile.role

            # 👨‍💼 MANAGER / HR / SALES / HEADS
            if role in [
                'PracticeHead',
                'PrincipalSoftwareEngineer',
                'HR',
                'Sales',
                'Manager',
            ]:

                tasks = TimeSheet.objects.filter(
                    user__employeeprofile__reporting_manager=user
                ).order_by("-id")

            # 👤 EMPLOYEE → ONLY 1 RECORD (FIX HERE)
            else:
                tasks = TimeSheet.objects.filter(
                    user=user
                ).order_by("-id")[:1]

        except EmployeeProfile.DoesNotExist:

            role = "employee"
            tasks = TimeSheet.objects.filter(
                user=user
            ).order_by("-id")[:1]

    return render(
        request,
        'home.html',
        {
            'tasks': tasks,
            'role': role
        }
    )
