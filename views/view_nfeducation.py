from django.shortcuts import render,redirect
from employee.models import Employee, NonFormalEducation
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from employee.forms import NFEducationForm
from django.core.exceptions import ObjectDoesNotExist


#Your Code Here


def detailEmployeeNFormalEducation(request, id):
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    data = NonFormalEducation.objects.filter(employee=employeeData).order_by('-id')

    context = {
        "employeeData" : employeeData,
        "data" : data,
        "pajina_employee" : "active",
        "tab_nfeducation" : "active",
            }
    return render(request, 'employee/detail_employee.html',context)


def addNewNFormalEducation(request, id):
    id = decrypt_id(id)
	
    employeeData = Employee.objects.get(id=id)
	
    if request.method == 'POST':
        form = NFEducationForm(request.POST)
        instance = form.save(commit=False)
        instance.employee_id = id
        instance.created_by = request.user
        instance.save()
        messages.success(request, f'Formal Education add sucessfuly')
        return redirect('employee:detailEmployeeNFormalEducation', id=encrypt_id(id))
    else:
        form = NFEducationForm()
    context = {
        'employeeData': employeeData,
        'form': form,
        'title': 'Add Non Formal Education',
        'legend': 'Aumenta Salariu'
    }
    return render(request, 'employee/add_employeefeducation.html', context)