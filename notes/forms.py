from django.forms import ModelForm
from .models import notes
from django import forms
class NotesForm(ModelForm):
    class Meta:
        model = notes
        fields = ['notes_title','notes']
        labels = {
            'notes_title': 'Notes title',
            'notes': 'Notes',}
        widgets={
            'notes_title': forms.TextInput({'class':"w-full mt-2 px-5 rounded-xl"}),
            'notes': forms.ClearableFileInput({'class':"w-full mt-2 px-5 rounded-xl",'multiple':True})}