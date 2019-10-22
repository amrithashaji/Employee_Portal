from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Employee
import requests
import json


# Create your views here.
@login_required(redirect_field_name='/login/')
def index(request, template_name='employee/home.html'):
    """ View for rendering home page"""
    return render(request, template_name)

@login_required(redirect_field_name='/login/')
def employeDetails(request, empid, template_name='employee/employe_details.html'):
    """ View for rendering Employee details page"""

    return render(request, template_name, {'empid':empid})

@login_required(redirect_field_name='/login/')
def add_employee(request, template_name='employee/add_employee.html'):
    """ This view to create new employ"""

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')
        ph = request.POST.get('ph')
        address = request.POST.get('addr')
        photo = request.POST.get('photo')

        createEmployee = Employee.objects.create(
            employee_name = name,
            image_as_a_blob = photo,
            email = email,
            password = pswd,
            phone = ph,
            address  = address
        )

        createEmployee.save()
        return redirect('/home/')

    return render(request, template_name)

