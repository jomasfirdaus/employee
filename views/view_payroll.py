from django.shortcuts import render,redirect
from employee.models import *
from payroll.models import Salary
from django.contrib import messages
from settingapps.utils import  decrypt_id, encrypt_id
from payroll.forms import SalaryForm
from contract.models import Contract


#Your Code Here


def detailEmployeePayroll(request, id):
    id = decrypt_id(id)
    employeeData = Employee.objects.get(id=id)
    contractData = Contract.objects.get(employeeuser__employee=employeeData, is_active=True)
    payrolllist = Salary.objects.filter(contract=contractData).order_by('-id')

    context = {
        "employeeData" : employeeData,
        "payrolllist" : payrolllist,
        "pajina_employee" : "active",
        "tab_payroll" : "active",
            }
    return render(request, 'employee/detail_employee.html',context)


def viewPayrollPerContract(request, id, id_employee):
    id = decrypt_id(id)
    id_employee = decrypt_id(id_employee)

    employeeData = Employee.objects.get(id=id_employee)
    contractData = Contract.objects.get(id=id)
    payrolllist = Salary.objects.filter(contract=contractData).order_by('-id')

    context = {
        "employeeData" : employeeData,
        "payrolllist" : payrolllist,
        "pajina_employee" : "active",
        "tab_payroll" : "active",
        "non": 'non',
    }
    return render(request, 'employee/detail_employee.html',context)


def addNewPayroll(request, id, id_employee):
    id = decrypt_id(id)
    id_employee = decrypt_id(id_employee)
	
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
        return redirect('employee:detailEmployeePayroll', id=encrypt_id(id_employee))
    else:
        form = SalaryForm()
    context = {
        'cont': contract,
        'form': form,
        'title': 'Add New Payroll',
    }
    return render(request, 'employee/formulariu.html', context)