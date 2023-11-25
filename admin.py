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


class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language
class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource
admin.site.register(Language, LanguageAdmin)


class AreaResource(resources.ModelResource):
    class Meta:
        model = Area
class AreaAdmin(ImportExportModelAdmin):
    resource_class = AreaResource
admin.site.register(Area, AreaAdmin)


class UniversityResource(resources.ModelResource):
    class Meta:
        model = University
class UniversityAdmin(ImportExportModelAdmin):
    resource_class = UniversityResource
admin.site.register(University, UniversityAdmin)


class EducationLevelResource(resources.ModelResource):
    class Meta:
        model = EducationLevel
class EducationLevelAdmin(ImportExportModelAdmin):
    resource_class = EducationLevelResource
admin.site.register(EducationLevel, EducationLevelAdmin)


class FamilyRelationResource(resources.ModelResource):
    class Meta:
        model = FamilyRelation
class FamilyRelationAdmin(ImportExportModelAdmin):
    resource_class = FamilyRelationResource
admin.site.register(FamilyRelation, FamilyRelationAdmin)


class FormalEducationResource(resources.ModelResource):
    class Meta:
        model = FormalEducation
class FormalEducationAdmin(ImportExportModelAdmin):
    resource_class = FormalEducationResource
admin.site.register(FormalEducation, FormalEducationAdmin)


class NonFormalEducationResource(resources.ModelResource):
    class Meta:
        model = NonFormalEducation
class NonFormalEducationAdmin(ImportExportModelAdmin):
    resource_class = NonFormalEducationResource
admin.site.register(NonFormalEducation, NonFormalEducationAdmin)


class WorkExperienceResource(resources.ModelResource):
    class Meta:
        model = WorkExperience
class WorkExperienceAdmin(ImportExportModelAdmin):
    resource_class = WorkExperienceResource
admin.site.register(WorkExperience, WorkExperienceAdmin)


class EmpLanguageResource(resources.ModelResource):
    class Meta:
        model = EmpLanguage
class EmpLanguageAdmin(ImportExportModelAdmin):
    resource_class = EmpLanguageResource
admin.site.register(EmpLanguage, EmpLanguageAdmin)


