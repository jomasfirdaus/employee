# Generated by Django 4.2.6 on 2023-11-07 15:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='Employee ID')),
                ('identify_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='Identify ID')),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('pob', models.CharField(blank=True, max_length=100, null=True, verbose_name='Place of birth')),
                ('dob', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('marital', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorce', 'Divorce'), ('Widow', 'Widow')], max_length=15, null=True, verbose_name='Marital Status')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('personal_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('oficial_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('blood', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=15, null=True)),
                ('father', models.CharField(blank=True, max_length=100, null=True)),
                ('mother', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='funsionariu/foto', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employeecountry', to='custom.country')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employeecreatedbys', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employeedeletedbys', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Employeeupdatetedbys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '1-Data-Employee-Employee',
            },
            managers=[
                ('default_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeUsercreatedbys', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeUserdeletedbys', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeUserupdatetedbys', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('default_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
