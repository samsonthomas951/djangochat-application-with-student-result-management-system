from django.forms import ModelForm
from django import forms
from .models import StudentClass

class StudentClassForm(ModelForm):
    class Meta:
        model = StudentClass
        fields = ['class_name','class_name_in_numeric','section']