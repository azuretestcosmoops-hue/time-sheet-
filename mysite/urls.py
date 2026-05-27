from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from employee_timesheet import views as emp_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout (FIXED - custom view to avoid 405 error)
    path('logout/', emp_views.logout_view, name='logout'),

    # App routes
    path('', include('employee_timesheet.urls')),
]
