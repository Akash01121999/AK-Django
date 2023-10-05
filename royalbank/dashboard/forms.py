from django import forms
from .models import user,complaint
 
 
class login(forms.ModelForm):
    class Meta:
        model=user
        fields=['userid']


class complaintForm(forms.ModelForm):
        class Meta:
            model=complaint
            fields=['com_letter']
