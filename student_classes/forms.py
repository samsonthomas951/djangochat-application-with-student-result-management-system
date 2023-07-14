from django.forms import ModelForm
from django import forms
from .models import StudentClass

class StudentClassForm(ModelForm):
    class Meta:
        model = StudentClass
        fields = ['class_name','class_name_in_numeric','section']
        # widgets = {
        #     'class_name': forms.Select({'class': "w-full mt-2 px-5 rounded-xl"}),
        #     'class_name_in_numeric':  forms.Select({'class': "w-full mt-2 px-5 rounded-xl"}),
        #     'section':  forms.Select({'class': "w-full mt-2 px-5 rounded-xl"}),
        # } 
        widgets = {
            'class_name': forms.TextInput({'class': "w-full mt-2 px-5 rounded-xl"}),
            'class_name_in_numeric':  forms.NumberInput({'class': "w-full mt-2 px-5 rounded-xl"}),
            'section':  forms.TextInput({'class': "w-full mt-2 px-5 rounded-xl"}),
        }