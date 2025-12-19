from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee

def home(request):
  #return HttpResponse("Hello")
  employees = Employee.objects.all()
  context = {
    'employees': employees
  }
  return render(request, 'home.html', context)

