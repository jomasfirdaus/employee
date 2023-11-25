from django.shortcuts import render,redirect
from employee.models import *
from payroll.models import Salary
from custom.models import Department, Position, RequestSet
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from payroll.forms import SalaryForm
from django.core.exceptions import ObjectDoesNotExist


#Your Code Here


def detailEmployeePayroll(request, id):
    group = request.user.groups.all()[0].name
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    payrolllist = Salary.objects.all().order_by('-id')

    context = {
        "employeeData" : employeeData,
        "payrolllist" : payrolllist,
        "pajina_employee" : "active",
        "tab_payroll" : "active",
            }
    return render(request, 'employee/detail_employee.html',context)


def addNewPayroll(request, id):
    id = decrypt_id(id)
	
    contract = Contract.objects.get(id=id)
	
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        instance = form.save(commit=False)
        tax = 0
        if instance.gross > 500:
            tax = float(instance.gross)-500
            tax = tax * 0.1
        social = float(instance.gross) * 0.04
        net = float(instance.gross) - tax - social

        instance.contract = contract
        instance.tax = tax
        instance.social = social
        instance.net = net
        instance.created_by = request.user
        instance.save()
        messages.success(request, f'Payroll add sucessfuly')
        return redirect('employee:detailEmployeePayroll', id=encrypt_id(id))
    else:
        form = SalaryForm()
    context = {
        'cont': contract,
        'form': form,
        'title': 'Add Payroll',
        'legend': 'Aumenta Salariu'
    }
    return render(request, 'employee/add_employeepayroll.html', context)