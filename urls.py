from django.urls import path 

from employee import views
from contract import *

app_name = "employee"


urlpatterns = [
	path('employee/list/employee', views.listaEmployee, name='listaEmployee'),
	path('add/employee', views.addEmployee, name='addEmployee'),
	path('edit/employee/<str:id>/', views.editEmployee, name='editEmployee'),
    
	path('detail/employee/<str:id>/', views.detailEmployee, name='detailEmployee'),
    
	path('detail/employee/contract/<str:id>/', views.detailEmployeeContract, name='detailEmployeeContract'),
	path('detail/employee/add/new/contract/<str:id>/', views.addNewContract, name='addNewContract'),
    
	path('detail/employee/payroll/<str:id>/', views.detailEmployeePayroll, name='detailEmployeePayroll'),
	path('detail/employee/payroll/add/payroll/<str:id>/', views.addNewPayroll, name='addNewPayroll'),
    
	path('detail/employee/formal/education/<str:id>/', views.detailEmployeeFormalEducation, name='detailEmployeeFormalEducation'),
	path('detail/employee/formal/education/add/formal/education/<str:id>/', views.addNewFormalEducation, name='addNewFormalEducation'),
    
	path('detail/employee/nonformal/education/<str:id>/', views.detailEmployeeNFormalEducation, name='detailEmployeeNFormalEducation'),
	path('detail/employee/nonformal/education/add/nonformal/education/<str:id>/', views.addNewNFormalEducation, name='addNewNFormalEducation'),
    
	path('detail/employee/work/experience/<str:id>/', views.detailEmployeeWorkExperience, name='detailEmployeeWorkExperience'),
	path('detail/employee/work/experience/add/work/experience/<str:id>/', views.addNewWorkExperience, name='addNewWorkExperience'),
    
	path('detail/employee/language/skills/<str:id>/', views.detailEmployeeLanguageSkills, name='detailEmployeeLanguageSkills'),
	path('detail/employee/language/skills/add/language/skills/<str:id>/', views.addNewLanguageSkills, name='addNewLanguageSkills'),
    
	path('detail/employee/criminal/record/<str:id>/', views.detailEmployeeCriminalRecord, name='detailEmployeeCriminalRecord'),
	path('detail/employee/criminal/record/add/criminal/record/<str:id>/', views.addNewCriminalRecord, name='addNewCriminalRecord'),
    
	path('detail/employee/capacity/building/<str:id>/', views.detailEmployeeCapacityBuilding, name='detailEmployeeCapacityBuilding'),
	path('detail/employee/capacity/building/add/capacity/building/<str:id>/', views.addNewCapacityBuilding, name='addNewCapacityBuilding'),
    
	path('detail/employee/session/refresher/<str:id>/', views.detailEmployeeSessionRefresher, name='detailEmployeeSessionRefresher'),
	path('detail/employee/session/refresher/add/session/refresher/<str:id>/', views.addNewSessionRefresher, name='addNewSessionRefresher'),
    
    
	path('detail/employee/create/new/user/<str:id>/', views.createnewuser, name='createnewuser'),
	path('detail/employee/change/user/<str:id_employee>/<str:id_contract>/', views.changeuser, name='changeuser'),
    
	# path('edit/item/travel/<str:id_item>/', views.edititemtravel, name='edititemtravel'),
	# path('apaga/item/travel/<str:id_item>/', views.apagaitemtravel, name='apagaitemtravel'),
	# path('aproved/item/travel/<str:id_item>/', views.aproveditemtravel, name='aproveditemtravel'),
	# path('riject/item/travel/<str:id_item>/', views.rijectitemtravel, name='rijectitemtravel'),
	# path('deliver/item/travel/<str:id_item>/', views.deliveritemtravel, name='deliveritemtravel'),
	# path('send/travel/request/<str:id>/', views.sendtravelrequest, name='sendtravelrequest'),


	# path('acepted/travel/request/<str:id>/', views.aceptedtravelrequest, name='aceptedtravelrequest'),
	# path('rijected/travel/request<str:id>/', views.rijectedtravelrequest, name='rijectedtravelrequest'),
]

