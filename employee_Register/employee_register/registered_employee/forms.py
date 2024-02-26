from django import forms
from .models import EMployeeRegistrationsModel

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = EMployeeRegistrationsModel
        fields = ('employeeName','employeeAge','employeeCode','employeeCurrentPosition')
        labels = {
            'employeeName':'Full Name',
            'employeeCode':'EMP. Code'
        } 
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['employeeCurrentPosition'].empty_label = "Select"
        self.fields['employeeCode'].required = False