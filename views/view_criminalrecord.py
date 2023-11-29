from django.shortcuts import render,redirect
from employee.models import Employee
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from employee.forms import CriminalRecordForm
from employee.models import CriminalRecord


#Your Code Here


def detailEmployeeCriminalRecord(request, id):
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    data = CriminalRecord.objects.filter(employee=employeeData).order_by('-id')

    context = {
        "employeeData" : employeeData,
        "data" : data,
        "pajina_employee" : "active",
        "tab_criminalrecord" : "active",
            }
    return render(request, 'employee/detail_employee.html',context)


def addNewCriminalRecord(request, id):
    id = decrypt_id(id)

    form = CriminalRecordForm()
	
    employeeData = Employee.objects.get(id=id)
	
    if request.method == 'POST':
        form = CriminalRecordForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.employee_id = id
            instance.created_by = request.user
            instance.save()
            messages.success(request, f'Capacity Building add sucessfuly')
            return redirect('employee:detailEmployeeCriminalRecord', id=encrypt_id(id))
        else:
            error_messages = []  # Initialize an empty list to store custom error messages
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field}: {error}")
            print(str(error_messages))
            messages.error(request, 'There was an error. Please correct the form.')  # Error message
    else:
        form = CriminalRecordForm()
    context = {
        'employeeData': employeeData,
        'form': form,
        'title': 'Add Non Formal Education',
        'legend': 'Aumenta Salariu'
    }
    return render(request, 'employee/add_employeelanguageskills.html', context)