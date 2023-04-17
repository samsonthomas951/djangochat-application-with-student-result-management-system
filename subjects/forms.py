from django.forms import ModelForm
from django import forms
from .models import Subject, SubjectCombination

class subjectform(ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name','subject_code']
        labels = {
            'subject_name': 'Subject Name',
            'subject_code': 'Subject code',            
        }        
        
        widgets={
            'subject_name': forms.TextInput({'class':"w-full mt-2 px-5 rounded-xl"}),
            'subject_code':  forms.NumberInput({'class':"w-full mt-2 px-5 rounded-xl"}),
        }

class SubjectCombinationForm(ModelForm):
    class Meta:
        model = SubjectCombination
        fields = ['select_class', 'select_subject']
        widgets = {
            'select_class': forms.Select({'class': "w-full mt-2 px-5 rounded-xl"}),
            'select_subject':  forms.Select({'class': "w-full mt-2 px-5 rounded-xl"}),
        }        