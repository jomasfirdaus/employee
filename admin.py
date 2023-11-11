from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from employee.models import *
from import_export import resources

# Register your models here.
class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
admin.site.register(Employee, EmployeeAdmin)


admin.site.register(EmployeeUser)



