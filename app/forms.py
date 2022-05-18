from django import forms

from .models import Job, Company, UserResume, UserFormation, UserExperience

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company']
        
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'cnpj']
        
class UserResumeForm(forms.ModelForm):
    class Meta:
        model = UserResume
        fields = ['gitHub', 'linkedIn', 'age', 'description', 'certifications', 'addittional_info']
        
class UserFormationForm(forms.ModelForm):
    class Meta:
        model = UserFormation
        fields = ['institution', 'course', 'start_date', 'end_date']
        
class UserExperienceForm(forms.ModelForm):
    class Meta:
        model = UserExperience
        fields = ['company', 'occupation', 'start_date', 'end_date']