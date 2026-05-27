from django.urls import path
from . import views

urlpatterns = [
    # Dashboard page
    path('', views.dashboard, name='dashboard'),

    # Add task page
    path('add/', views.add_task, name='add_task'),

    # Delete task (NEW)
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
