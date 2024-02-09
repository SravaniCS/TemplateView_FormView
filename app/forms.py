from django import forms
from app.models import *

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'