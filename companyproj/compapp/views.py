from django.shortcuts import render

# Create your views here.
from .models import Employee

def employee_view(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})