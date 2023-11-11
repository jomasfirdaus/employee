from django import forms
from rekrutamentu.models import UserApplication, UserAttachment
from django.forms import inlineformset_factory
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Button, Div, Field
from employee.models import *



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # You can specify the fields you want to include if needed

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('emp_id', css_class='col-md-4'),
                Column('identify_id', css_class='col-md-4'),
            ),

            Row(
                Column('first_name', css_class='col-md-6'),
                Column('last_name', css_class='col-md-6'),
            ),

            Row(
                Column('address', css_class='col-md-6'),
            ),
            
            Row(
                Column('pob', css_class='col-md-6'),
                Column('dob', css_class='col-md-6'),
            ),
            
            Row(
                Column('sex', css_class='col-md-4'),
                Column('marital', css_class='col-md-4'),
                Column('blood', css_class='col-md-4'),
            ),
            
            Row(
                Column('personal_email', css_class='col-md-6'),
                Column('oficial_email', css_class='col-md-6'),
            ),
            
            Row(
                Column('father', css_class='col-md-6'),
                Column('mother', css_class='col-md-6'),
            ),
            
            Row(
                Column('country', css_class='col-md-6'),
                Column('image', css_class='col-md-6'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['emp_id'].widget.attrs['class'] = 'form-control'
        self.fields['identify_id'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['pob'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.input_type = 'date'
        self.fields['sex'].widget.attrs['class'] = 'form-control'
        self.fields['marital'].widget.attrs['class'] = 'form-control'
        self.fields['blood'].widget.attrs['class'] = 'form-control'
        self.fields['personal_email'].widget.attrs['class'] = 'form-control'
        self.fields['oficial_email'].widget.attrs['class'] = 'form-control'
        self.fields['father'].widget.attrs['class'] = 'form-control'
        self.fields['mother'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
  


class EmployeeUserForm(forms.ModelForm):
    class Meta:
        model = EmployeeUser
        fields = '__all__'  # You can specify the fields you want to include if needed

    def __init__(self, *args, **kwargs):
        super(EmployeeUserForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('emp_id', css_class='col-md-4'),
                Column('identify_id', css_class='col-md-4'),
            ),

            Row(
                Column('first_name', css_class='col-md-6'),
                Column('last_name', css_class='col-md-6'),
            ),

            Row(
                Column('address', css_class='col-md-6'),
            ),
            
            Row(
                Column('pob', css_class='col-md-6'),
                Column('dob', css_class='col-md-6'),
            ),
            
            Row(
                Column('sex', css_class='col-md-4'),
                Column('marital', css_class='col-md-4'),
                Column('blood', css_class='col-md-4'),
            ),
            
            Row(
                Column('personal_email', css_class='col-md-6'),
                Column('oficial_email', css_class='col-md-6'),
            ),
            
            Row(
                Column('father', css_class='col-md-6'),
                Column('mother', css_class='col-md-6'),
            ),
            
            Row(
                Column('country', css_class='col-md-6'),
                Column('image', css_class='col-md-6'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['emp_id'].widget.attrs['class'] = 'form-control'
        self.fields['identify_id'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['pob'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.input_type = 'date'
        self.fields['sex'].widget.attrs['class'] = 'form-control'
        self.fields['marital'].widget.attrs['class'] = 'form-control'
        self.fields['blood'].widget.attrs['class'] = 'form-control'
        self.fields['personal_email'].widget.attrs['class'] = 'form-control'
        self.fields['oficial_email'].widget.attrs['class'] = 'form-control'
        self.fields['father'].widget.attrs['class'] = 'form-control'
        self.fields['mother'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'