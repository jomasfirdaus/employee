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

