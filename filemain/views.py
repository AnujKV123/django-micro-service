from django.shortcuts import render, redirect
from .models import Employee
from rest_framework import viewsets
from . serializers import EmployeeSerializers

# Create your views here.
def index(request):
    return render(request, "index.html")

def Save_data(request):
    # get the values from input form
    if request.method == "POST":
        emp_email = request.POST['Emp_email'] #origins
        emp_name = request.POST['Emp_name'] #destination1
        emp_profile = request.POST['Emp_profile'] #destination2
        EmpData = Employee(email=emp_email, name=emp_name, profile=emp_profile)
        EmpData.save()
        return render(request, "success.html")
    else:
        return redirect("/")
    
class EmployeeViewsets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
