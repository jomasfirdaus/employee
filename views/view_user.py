from django.shortcuts import render,redirect
from employee.models import *
from contract.models import Contract
from custom.models import RequestSet
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from employee.forms import EmployeeForm
from django.core.exceptions import ObjectDoesNotExist


#Your Code Here

def createnewuser(request, id):
    id = decrypt_id(id)
    employee = Employee.objects.get(pk=id)

    if request.method == 'POST':
        # Foti variable hosi Form
        user = request.POST.get('user')
        password = request.POST.get('password')
        password = make_password(password)
        auth_group_id = request.POST.get('auth_group')
        
        # Save ba Model User
        user = User(username=user, password=password, first_name=employee.first_name, last_name=employee.last_name)
        user.save()

        # Set UserGroup
        groupuser = Group.objects.get(id=auth_group_id)
        lastid = User.objects.all().last()
        user = User.objects.get(id=lastid.id)
        user.groups.add(groupuser)

        employeeuser = EmployeeUser.objects.get(employee__id=employee.id)
        employeeuser.user=lastid
        employeeuser.updated_by = request.user
        employeeuser.save()


        return redirect('employee:detailEmployeeContract', id=encrypt_id(id))
    else:
        auth_groups = Group.objects.all()
        context = {
            "id": id,
            "auth_groups" : auth_groups,
            "pajina_employee" : "active",
            'title': 'Add New user',
    }
    return render(request, 'employee/formulariu.html', context)

def changeuser(request, id_employee, id_contract):
    id_employee = decrypt_id(id_employee)
    id_contract = decrypt_id(id_contract)
    
    employee = Employee.objects.get(pk=id_employee)

    if request.method == 'POST':
        # Foti variable hosi Form
        username = request.POST.get('user')
        password = request.POST.get('password')
        password = make_password(password)
        auth_group_id = request.POST.get('auth_group')

        # Dezativa atual user
        emUser = EmployeeUser.objects.filter(employee__id=id_employee)
        for dadus in emUser.iterator():
            user = User.objects.get(id=dadus.user_id)
            user.is_active = False
            user.save()

        # Kria User foun
        userId = User.objects.all().last()
        newuserid = userId.id + 1

        user = User()
        user.id = newuserid
        user.username = str(employee.first_name) + str(newuserid)
        user.password = make_password('password')
        user.first_name = employee.first_name
        user.last_name = employee.last_name
        user.save()

        # Set UserGroup ba Userfoun
        groupuser = Group.objects.get(id=auth_group_id)
        user = User.objects.get(id=newuserid)
        user.groups.add(groupuser)

        # Kria Employee User hosi employee
        empuserId = EmployeeUser.objects.all().last()
        newempuserid = empuserId.id + 1
        employeeuser = EmployeeUser()
        employeeuser.id = newempuserid
        employeeuser.user = User.objects.get(id=newuserid)
        employeeuser.employee = Employee.objects.get(id=id_employee)
        employeeuser.created_by = request.user
        employeeuser.save()

        contract = Contract.objects.get(id=id_contract)
        contract.employeeuser = EmployeeUser.objects.get(id=newempuserid)
        contract.save()


        return redirect('employee:detailEmployeeContract', id=encrypt_id(id_employee))
    else:
        auth_groups = Group.objects.all()
        context = {
            "d": id,
            "auth_groups" : auth_groups,
            "pajina_employee" : "active",
        }
        return render(request, 'employee/add_user.html',context)