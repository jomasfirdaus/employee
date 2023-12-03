from django.shortcuts import render,redirect
from employee.models import *
from contract.models import Contract
from custom.models import Department, Position, RequestSet
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from contract.forms import ContractForm, TerminateContractForm
from django.core.exceptions import ObjectDoesNotExist


#Your Code Here


def detailEmployeeContract(request, id):
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    contractEmployee = Contract.objects.filter(employeeuser__employee__id=employeeData.id).order_by('-id')

    context = {
        "employeeData" : employeeData,
        "contractEmployee" : contractEmployee,
        "pajina_employee" : "active",
        "tab_contract" : "active",
            }
    return render(request, 'employee/detail_employee.html',context)


def addNewContract(request, id):
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    lastid = EmployeeUser.objects.all().last()
    if lastid:
        lastid = lastid.id + 1
    else:
        lastid = 1
    employeeContract = 'mamuk'
    lastContract = Contract.objects.filter(employeeuser__employee__id=id).count()
    if lastContract > 0:
        employeeContract = 'iha'
    form = ContractForm()

    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():

            instance = form.save(commit=False)

            if employeeContract == 'iha':
                instance.employeeuser = EmployeeUser.objects.filter(employee__id=id).last()
            else:
                # Kria User foun
                userId = User.objects.all().last()
                newuserid = userId.id + 1

                user = User()
                user.id = newuserid
                user.username = str(employeeData.first_name) + str(newuserid)
                user.password = make_password('password')
                user.first_name = employeeData.first_name
                user.last_name = employeeData.last_name
                user.save()

                # Set UserGroup ba Userfoun
                position = Position.objects.get(id=int(request.POST['position']))
                # department = Department.objects.get(id=int(request.POST['department']))

                is_executive = request.POST['is_executive']

                strap_position = position.name.replace(" ","_")
                # strap_department = department.name.replace(" ","_")

                if is_executive == "true":
                    groupname = str("Executive")+str("_")+str(strap_position)
                    if instance.department is not None:
                        messages.success(request, 'Sorry! Executive does not have department. Please check your form')  # Success message
                        return redirect('employee:addNewContract', id=encrypt_id(id))
                else:
                    department = Department.objects.get(id=int(request.POST['department']))
                    strap_department = department.name.replace(" ","_")
                    groupname = str(strap_position)+str("_")+str(strap_department)

                groupname = Group.objects.get(name=groupname)

                user = User.objects.get(id=newuserid)
                user.groups.add(groupname)
                

                useremployee = EmployeeUser()
                useremployee.user_id = newuserid
                useremployee.employee_id = employeeData.id
                useremployee.id = lastid
                useremployee.created_by = User.objects.get(id=request.user.id)
                useremployee.save()
                instance.employeeuser = EmployeeUser.objects.get(id=lastid)

            try:
                contract = Contract.objects.get(employeeuser__employee__id=id, is_active=True)
                contract.is_active = False
                contract.save()
            except:
                print('')
            instance.created_by = User.objects.get(id=request.user.id)
            instance.is_active = True
            instance.save()
            messages.success(request, 'Employee created successfully.')  # Success message
            return redirect('employee:detailEmployeeContract', id=encrypt_id(id))
        else:
            error_messages = []  # Initialize an empty list to store custom error messages
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field}: {error}")
            print(str(error_messages))
            messages.error(request, 'There was an error. Please correct the form.')  # Error message
            return redirect('employee:addNewContract', id=encrypt_id(id))

    context = {
        "form" : form,
        "pajina_employee" : "active",
        'title': 'Add New Contract',
    }
    return render(request, 'employee/formulariu.html', context)



def terminateContract(request, id, id_employee):
    id = decrypt_id(id)
    id_employee = decrypt_id(id_employee)

    contract = Contract.objects.get(id=id)
    
    form = TerminateContractForm()

    if request.method == 'POST':
        form = TerminateContractForm(request.POST, instance=contract)  # Menggunakan instance=contract
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_active = False
            instance.updated_by = request.user
            instance.save()
            
            messages.error(request, 'Terminate Contract Successfully.')  # Error message
            return redirect('employee:detailEmployeeContract', id=encrypt_id(id_employee))
        else:
            error_messages = []  # Initialize an empty list to store custom error messages
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field}: {error}")
            print(str(error_messages))
            messages.error(request, 'There was an error. Please correct the form.')  # Error message
            return redirect('employee:terminateContract', id=encrypt_id(id), id_employee = encrypt_id(id_employee))

    context = {
        "form" : form,
        "pajina_employee" : "active",
        'title': 'Add New Contract',
    }
    return render(request, 'employee/formulariu.html', context)