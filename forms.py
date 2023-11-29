from django import forms
from rekrutamentu.models import UserApplication, UserAttachment
from django.forms import inlineformset_factory
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Button, Div, Field
from employee.models import *
from payroll.models import Salary



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
                Column('social_id', css_class='col-md-4'),
            ),

            Row(
                Column('first_name', css_class='col-md-6'),
                Column('last_name', css_class='col-md-6'),
            ),

            Row(
                Column('address', css_class='col-md-3'),
                Column('munisipiu', css_class='col-md-3'),
                Column('postu', css_class='col-md-3'),
                Column('suku', css_class='col-md-3'),
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
            ),
            
            Row(
                Column('image', css_class='col-md-6'),
                Column('signature', css_class='col-md-6'),
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
        self.fields['social_id'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['munisipiu'].widget.attrs['class'] = 'form-control'
        self.fields['postu'].widget.attrs['class'] = 'form-control'
        self.fields['suku'].widget.attrs['class'] = 'form-control'
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
        

class SalaryForm(forms.ModelForm):
	class Meta:
		model = Salary
		fields = ['gross']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.fields['gross'].required = True
		self.helper.layout = Layout(
			Row(
				Column('gross', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit" title="Rai">Save <i class="fa fa-save"></i></button> """)
		)
          

class FEducationForm(forms.ModelForm):
    class Meta:
        model = FormalEducation
        fields = '__all__'  # You can specify the fields you want to include if needed
        exclude = ['employee']

    def __init__(self, *args, **kwargs):
        super(FEducationForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('educationlevel', css_class='col-md-4'),
            ),

            Row(
                Column('university', css_class='col-md-4'),
                Column('faculty', css_class='col-md-4'),
                Column('department', css_class='col-md-4'),
            ),

            Row(
                Column('area', css_class='col-md-4'),
                Column('graduation_year', css_class='col-md-4'),
                Column('year', css_class='col-md-4'),
            ),
            
            Row(
                Column('file', css_class='col-md-6'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['educationlevel'].widget.attrs['class'] = 'form-control'
        self.fields['university'].widget.attrs['class'] = 'form-control'
        self.fields['faculty'].widget.attrs['class'] = 'form-control'
        self.fields['department'].widget.attrs['class'] = 'form-control'
        self.fields['area'].widget.attrs['class'] = 'form-control'
        self.fields['graduation_year'].widget.input_type = 'date'
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['class'] = 'form-control'


class NFEducationForm(forms.ModelForm):
    class Meta:
        model = NonFormalEducation
        fields = '__all__'  # You can specify the fields you want to include if needed
        exclude = ['employee']

    def __init__(self, *args, **kwargs):
        super(NFEducationForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('title', css_class='col-md-4'),
                Column('tutelary_entity', css_class='col-md-4'),
                Column('area', css_class='col-md-4'),
            ),

            Row(
                Column('start_date', css_class='col-md-4'),
                Column('end_date', css_class='col-md-4'),
                Column('hours', css_class='col-md-4'),
            ),

            Row(
                Column('year', css_class='col-md-4'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['tutelary_entity'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.input_type = 'date'
        self.fields['end_date'].widget.input_type = 'date'
        self.fields['area'].widget.attrs['class'] = 'form-control'
        self.fields['hours'].widget.attrs['class'] = 'form-control'
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['class'] = 'form-control'


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'  # You can specify the fields you want to include if needed
        exclude = ['employee']

    def __init__(self, *args, **kwargs):
        super(WorkExperienceForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('institute', css_class='col-md-4'),
                Column('department', css_class='col-md-4'),
            ),

            Row(
                Column('position', css_class='col-md-4'),
            ),

            Row(
                Column('start_date', css_class='col-md-4'),
                Column('end_date', css_class='col-md-4'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['institute'].widget.attrs['class'] = 'form-control'
        self.fields['department'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.input_type = 'date'
        self.fields['end_date'].widget.input_type = 'date'
        self.fields['position'].widget.attrs['class'] = 'form-control'


class EmpLanguageForm(forms.ModelForm):
    class Meta:
        model = EmpLanguage
        fields = '__all__'  # You can specify the fields you want to include if needed
        exclude = ['employee']

    def __init__(self, *args, **kwargs):
        super(EmpLanguageForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('language', css_class='col-md-4'),
            ),

            Row(
                Column('read', css_class='col-md-3'),
                Column('speak', css_class='col-md-3'),
                Column('write', css_class='col-md-3'),
                Column('file_language', css_class='col-md-3'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['language'].widget.attrs['class'] = 'form-control'
        self.fields['read'].widget.attrs['class'] = 'form-control'
        self.fields['speak'].widget.attrs['class'] = 'form-control'
        self.fields['write'].widget.attrs['class'] = 'form-control'
        self.fields['file_language'].widget.attrs['class'] = 'form-control'


class CriminalRecordForm(forms.ModelForm):
    class Meta:
        model = CriminalRecord
        fields = '__all__'  # You can specify the fields you want to include if needed
        exclude = ['employee']

    def __init__(self, *args, **kwargs):
        super(CriminalRecordForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('issue_by', css_class='col-md-4'),
            ),

            Row(
                Column('issue_at', css_class='col-md-4'),
                Column('expire_at', css_class='col-md-4'),
            ),

            Row(
                Column('file_criminal', css_class='col-md-4'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['issue_by'].widget.attrs['class'] = 'form-control'
        self.fields['issue_at'].widget.input_type = 'date'
        self.fields['expire_at'].widget.input_type = 'date'
        self.fields['file_criminal'].widget.attrs['class'] = 'form-control'


class CapacityBuildingForm(forms.ModelForm):
    class Meta:
        model = CapacityBuilding
        fields = '__all__'  # You can specify the fields you want to include if needed
        exclude = ['employee']

    def __init__(self, *args, **kwargs):
        super(CapacityBuildingForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('place', css_class='col-md-4'),
                Column('title', css_class='col-md-4'),
            ),

            Row(
                Column('start_date', css_class='col-md-4'),
                Column('end_date', css_class='col-md-4'),
            ),

            Row(
                Column('file_capacity', css_class='col-md-4'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['place'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.input_type = 'date'
        self.fields['end_date'].widget.input_type = 'date'
        self.fields['file_capacity'].widget.attrs['class'] = 'form-control'


class SessionRefresherForm(forms.ModelForm):
    class Meta:
        model = SessionRefresher
        fields = '__all__'  # You can specify the fields you want to include if needed
        exclude = ['employee']

    def __init__(self, *args, **kwargs):
        super(SessionRefresherForm, self).__init__(*args, **kwargs)

        # Create a form helper and specify the layout
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('place', css_class='col-md-4'),
                Column('title', css_class='col-md-4'),
            ),

            Row(
                Column('start_date', css_class='col-md-4'),
                Column('end_date', css_class='col-md-4'),
            ),

            Row(
                Column('file_refresher', css_class='col-md-4'),
            ),

            Div(
                Button('cancel', 'Kansela', css_class='btn-secondary btn-sm', onclick="window.history.back();"),
                Submit('post', 'Submete', css_class='btn-primary btn-sm'),
            
                css_class='text-right',
            ),
        )

        # Add CSS classes to form fields if needed
        self.fields['place'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.input_type = 'date'
        self.fields['end_date'].widget.input_type = 'date'
        self.fields['file_refresher'].widget.attrs['class'] = 'form-control'