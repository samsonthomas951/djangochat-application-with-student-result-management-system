from django.forms import ModelForm
from students.models import Student
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['student_name','student_roll','student_email','student_gender','student_class','student_date_of_birth']
        labels = {
            'student_name': 'Student Name',
            'student_roll': 'Student Roll',
            'student_email':'Student emai' ,
            'student_gender':'Student gender' ,
            'student_class':'Student Class' ,
            'student_date_of_birth':'Student D.O.B',            
        }
        widgets={
            'student_name': forms.TextInput({'class':"w-full mt-2 px-5 rounded-xl"}),
            'student_roll': forms.TextInput({'class':"w-full mt-2 px-5 rounded-xl"}),
            'student_email': forms.EmailInput({'class':"w-full mt-2 px-5 rounded-xl"}),
            'student_gender': forms.Select({'class':"w-full mt-2 px-5 rounded-xl"}),
            'student_class': forms.Select({'class':"w-full mt-2 px-5 rounded-xl"}),
            'student_date_of_birth': forms.DateInput({'class':"w-full mt-2 px-5 rounded-xl"}),
        }