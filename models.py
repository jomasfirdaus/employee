import datetime
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from contract.models import Contract
from custom.models import Country, Year

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class Employee(models.Model):
    emp_id = models.CharField(max_length=10, null=True, blank=True, verbose_name="Employee ID")
    identify_id = models.CharField(max_length=10, null=True, blank=True, verbose_name="Identify ID")
    pin = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    pob = models.CharField(max_length=100, blank=True, null=True, verbose_name="Place of birth")
    dob = models.DateField(null=True, blank=True)
    sex = models.CharField(choices=[('Male','Male'),('Female','Female')], max_length=6, null=True, blank=True)
    marital = models.CharField(choices=[('Single','Single'),('Married','Married'),('Divorce','Divorce'),('Widow','Widow')], max_length=15, null=True, blank=False, verbose_name="Marital Status")
    phone = models.IntegerField(null=True, blank=True)
    personal_email = models.EmailField(null=True, blank=True)
    oficial_email = models.EmailField(null=True, blank=True)
    blood = models.CharField(choices=[('A','A'),('B','B'),('AB','AB'),('O','O')], max_length=15, null=True, blank=True)
    father = models.CharField(max_length=100, null=True, blank=True)
    mother = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=False, related_name="Employeecountry")
    image = models.ImageField(default='default.jpg', upload_to='funsionariu/foto', null=True,  blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    signature = models.ImageField(default='default.jpg', upload_to='funsionariu/signature', null=True,  blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Employeecreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Employeeupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Employeedeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)

    def age(self):
        if self.dob:
            return int(round((datetime.date.today() - self.dob).days/365.2425,0))
        else:
            return int(0)
    
    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='1-Data-Employee-Employee'



class EmployeeUser(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmployeeUsercreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmployeeUserupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmployeeUserdeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        template = '{0.employee}-{0.user}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()


class Language(models.Model):
    name = models.CharField(max_length=255, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Languagecreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Languageupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Languagedeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()


class Area(models.Model):
    name = models.CharField(max_length=255, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Areacreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Areaupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Areadeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()


class University(models.Model):
    name = models.CharField(max_length=255, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Universitycreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Universityupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Universitydeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()


class EducationLevel(models.Model):
    name = models.CharField(max_length=255, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EducationLevelcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EducationLevelupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EducationLeveldeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()


class FamilyRelation(models.Model):
    name = models.CharField(max_length=255, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="FamilyRelationcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="FamilyRelationupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="FamilyRelationdeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()


class FormalEducation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="FormalEducationemployee")
    educationlevel = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, related_name="FormalEducationeducationlevel")
    university = models.ForeignKey(University, null=True, blank=True, on_delete=models.CASCADE, related_name="FormalEducationuniversity")
    faculty = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    area =  models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True, related_name="FormalEducationarea")
    graduation_year = models.DateField(null=True, blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True, blank=True, related_name="FormalEducationyear")
    file = models.FileField(upload_to="upload_formal", null=True, blank=True,
    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Attach certificate")
    is_active = models.BooleanField(default=True)
    is_science = models.BooleanField(default=False, null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="FormalEducationcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="FormalEducationupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="FormalEducationdeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.educationlevel}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

class NonFormalEducation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="NonFormalEducationemployee")
    title = models.CharField(max_length=500, null=True, blank=True)
    tutelary_entity = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to="upload_nonformal", null=True, blank=True,
    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Attach certicate")
    is_active = models.BooleanField(default=True)
    traning_id = models.IntegerField(null=True, blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="NonFormalEducationcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="NonFormalEducationupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="NonFormalEducationdeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.title}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()


class WorkExperience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="WorkExperienceemployee")
    institute = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="WorkExperiencecreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="WorkExperienceupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="WorkExperiencedeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.employee}-{0.user}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()


class EmpLanguage(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="EmpLanguageeemployee")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpLanguagelanguage")
    speak = models.CharField(choices=[('Native','Native'),('Good','Good'),('Sufficient','Sufficient'),('Basic','Basic')], max_length=15, null=True, blank=True)
    read = models.CharField(choices=[('Native','Native'),('Good','Good'),('Sufficient','Sufficient'),('Basic','Basic')], max_length=15, null=True, blank=True)
    write = models.CharField(choices=[('Native','Native'),('Good','Good'),('Sufficient','Sufficient'),('Basic','Basic')], max_length=15, null=True, blank=True)
    file_language = models.FileField(upload_to='upload_languages', null=True, blank=True,
    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Attach Certificado")

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpLanguagecreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpLanguageupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="EmpLanguagedeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.contract}-{0.language}'
        return template.format(self)

    def delete(self, user):
        self.deleted_at = str(datetime.timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()
