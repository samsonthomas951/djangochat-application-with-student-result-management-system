from django.forms import ModelForm
from django import forms
from .models import DeclareResult

class DeclareResultForm(ModelForm):
    class Meta:
        model = DeclareResult
        fields = ['select_class', 'select_student']
        widgets = {
            'select_class': forms.Select({'class':"w-full mt-2 px-5 rounded-xl"}),
            'select_student':  forms.Select({'class':"w-full mt-2 px-5 rounded-xl"}),
        }
        labels = {
            'select_class' : 'Class',
            'select_student' : 'Select Student',
        }