from django.urls import path
from . import views
from django.conf import settings
from employee_app.employee_api import views as api_views


urlpatterns = [
    path('home/', views.index, name='index'),
    path('employeDetails/<str:empid>/', views.employeDetails, name='employeDetails'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('allEmployees/', api_views.allEmployees.as_view(), name='allEmployees'),
    path('detailsapi/<str:pk>/', api_views.detailsapi.as_view(), name='detailsapi'),
]

