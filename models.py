import datetime
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from custom.models import Country

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
