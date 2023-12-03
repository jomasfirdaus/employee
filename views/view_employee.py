from django.shortcuts import render,redirect
from employee.models import *
from contract.models import Contract
from custom.models import RequestSet
from django.contrib import messages
from settingapps.utils import  decrypt_id
from django.contrib.auth.models import User
from employee.forms import EmployeeForm
from django.core.exceptions import ObjectDoesNotExist


#Your Code Here

def listaEmployee(request):
    dadosem = Employee.objects.all().order_by('id')
    context = {
        "dadosem" : dadosem,
        "pajina_employee" : "active",
    }
    return render(request, 'employee/lista_employee.html',context)


def addEmployee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = User.objects.get(id=request.user.id) 
            instance.save()
            messages.success(request, 'Employee created successfully.')  # Success message
            return redirect('employee:listaEmployee')
        else:
            error_messages = []  # Initialize an empty list to store custom error messages
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field}: {error}")
            print(str(error_messages))
            messages.error(request, 'There was an error. Please correct the form.')  # Error message
            return redirect('employee:addEmployee')

    context = {
        "form" : form,
        "pajina_employee" : "active",
            }
    return render(request, 'employee/add_employee.html',context)


def editEmployee(request, id):
    id = decrypt_id(id)
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)  # Menggunakan instance=employee

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)  # Menggunakan instance=employee
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Employee updated successfully.')  # Pesan sukses
            return redirect('employee:listaEmployee')
        else:
            messages.error(request, 'There was an error. Please correct the form.')  # Pesan kesalahan
            return redirect('employee:editEmployee')

    context = {
        "form": form,
        "pajina_employee": "active",
        'title': 'Add Employee Data',
    }
    return render(request, 'employee/formulariu.html', context)


def detailEmployee(request, id):
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    employeeUser = EmployeeUser.objects.filter(employee=employeeData).last()
    employeeDataContract = Contract.objects.filter(employeeuser=employeeUser).order_by('-id').first()
    contractEmployee = Contract.objects.filter(employeeuser=employeeUser)

    context = {
        "employeeData" : employeeData,
        "employeeDataContract" : employeeDataContract,
        "contractEmployee" : contractEmployee,
        "pajina_employee" : "active",
        "tab_personal" : "active",
            }
    return render(request, 'employee/detail_employee.html',context)
