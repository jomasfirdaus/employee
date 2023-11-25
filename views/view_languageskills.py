from django.shortcuts import render,redirect
from employee.models import Employee, NonFormalEducation
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from employee.forms import EmpLanguageForm
from employee.models import EmpLanguage
from django.core.exceptions import ObjectDoesNotExist


#Your Code Here


def detailEmployeeLanguageSkills(request, id):
    group = request.user.groups.all()[0].name
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    data = EmpLanguage.objects.all().order_by('-id')

    context = {
        "employeeData" : employeeData,
        "data" : data,
        "pajina_employee" : "active",
        "tab_languageskills" : "active",
            }
    return render(request, 'employee/detail_employee.html',context)


def addNewLanguageSkills(request, id):
    id = decrypt_id(id)

    form = EmpLanguageForm()
	
    employeeData = Employee.objects.get(id=id)
	
    if request.method == 'POST':
        form = EmpLanguageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.employee_id = id
            instance.created_by = request.user
            instance.save()
            messages.success(request, f'Language Skills add sucessfuly')
            return redirect('employee:detailEmployeeLanguageSkills', id=encrypt_id(id))
        else:
            error_messages = []  # Initialize an empty list to store custom error messages
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field}: {error}")
            print(str(error_messages))
            messages.error(request, 'There was an error. Please correct the form.')  # Error message
    else:
        form = EmpLanguageForm()
    context = {
        'employeeData': employeeData,
        'form': form,
        'title': 'Add Non Formal Education',
        'legend': 'Aumenta Salariu'
    }
    return render(request, 'employee/add_employeelanguageskills.html', context)