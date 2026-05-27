from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('create/', views.create_timesheet, name='create_timesheet'),

    path('hr/', views.hr_dashboard, name='hr_dashboard'),

    path('sales/', views.sales_dashboard, name='sales_dashboard'),

    path('cfo/', views.cfo_dashboard, name='cfo_dashboard'),

    path('practice/', views.practice_dashboard, name='practice_dashboard'),

    path('manager/', views.manager_dashboard, name='manager_dashboard'),

]
