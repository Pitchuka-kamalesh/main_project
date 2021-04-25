from django import forms
from .models import Treatment_Model,PerformanceModel
from django.conf import settings

class Treatment_Form(forms.ModelForm):
    
    class Meta():
        model = Treatment_Model
        fields = '__all__'


class Performance_Form(forms.ModelForm):

    class Meta():
        model = PerformanceModel
        fields = '__all__'