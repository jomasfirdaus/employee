from django.shortcuts import render,redirect
from employee.models import Employee, FormalEducation
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from employee.forms import FEducationForm
from django.core.exceptions import ObjectDoesNotExist


#Your Code Here


def detailEmployeeFormalEducation(request, id):
    group = request.user.groups.all()[0].name
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    data = FormalEducation.objects.all().order_by('-id')

    context = {
        "employeeData" : employeeData,
        "data" : data,
        "pajina_employee" : "active",
        "tab_feducation" : "active",
            }
    return render(request, 'employee/detail_employee.html',context)


def addNewFormalEducation(request, id):
    id = decrypt_id(id)
	
    employeeData = Employee.objects.get(id=id)
	
    if request.method == 'POST':
        form = FEducationForm(request.POST)
        instance = form.save(commit=False)
        instance.employee_id = id
        instance.created_by = request.user
        instance.save()
        messages.success(request, f'Formal Education add sucessfuly')
        return redirect('employee:detailEmployeeFormalEducation', id=encrypt_id(id))
    else:
        form = FEducationForm()
    context = {
        'employeeData': employeeData,
        'form': form,
        'title': 'Add Payroll',
        'legend': 'Aumenta Salariu'
    }
    return render(request, 'employee/add_employeefeducation.html', context)