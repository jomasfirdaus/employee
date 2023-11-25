from django.shortcuts import render,redirect
from employee.models import Employee, NonFormalEducation
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from employee.forms import WorkExperienceForm
from employee.models import WorkExperience
from django.core.exceptions import ObjectDoesNotExist


#Your Code Here


def detailEmployeeWorkExperience(request, id):
    group = request.user.groups.all()[0].name
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    data = WorkExperience.objects.all().order_by('-id')

    context = {
        "employeeData" : employeeData,
        "data" : data,
        "pajina_employee" : "active",
        "tab_workexperience" : "active",
            }
    return render(request, 'employee/detail_employee.html',context)


def addNewWorkExperience(request, id):
    id = decrypt_id(id)

    form = WorkExperienceForm()
	
    employeeData = Employee.objects.get(id=id)
	
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.employee_id = id
            instance.created_by = request.user
            instance.save()
            messages.success(request, f'Work Experience add sucessfuly')
            return redirect('employee:detailEmployeeWorkExperience', id=encrypt_id(id))
        else:
            error_messages = []  # Initialize an empty list to store custom error messages
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field}: {error}")
            print(str(error_messages))
            messages.error(request, 'There was an error. Please correct the form.')  # Error message
    else:
        form = WorkExperienceForm()
    context = {
        'employeeData': employeeData,
        'form': form,
        'title': 'Add Non Formal Education',
        'legend': 'Aumenta Salariu'
    }
    return render(request, 'employee/add_employeefeducation.html', context)