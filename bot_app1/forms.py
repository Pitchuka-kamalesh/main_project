from django import forms
from .models import Treatment_Model


class Treatment_Form(forms.ModelForm):
    
    class Meta():
        model = Treatment_Model
        fields = '__all__'