from django.shortcuts import render, redirect
from .forms import NotesForm
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
import os
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import models
from pdf2image import convert_from_path
from django.core.files.storage import FileSystemStorage
def postnotes(request):
    if request.method =="POST":
        form=NotesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            users = User.objects.all()
            for user in users:
                title = request.POST['notes_title']
                subject = 'New material: "{} Notebooks"'.format(title)
                message = 'Hello {},\n\nNew notes have been posted.\nClick http://127.0.0.1:8000/postnotes/ to check them '.format(user.username)
                from_email = 'jumasam236@gmail.com'
                recipient_list = [user.email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)            
            uploaded_file = request.FILES['notes']
            if uploaded_file.content_type == 'application/pdf':
                return redirect("/")
    else:
        form = NotesForm()
    return render(request,'notes/notes_form.html',{'form':form,})
def notes(request):
    Notes = models.notes.objects.order_by('notes_title').values()
    template = loader.get_template('notes/notes.html')
    context = {
    'Notes': Notes
    }
    return HttpResponse(template.render(context, request))
def search_notes(request):
    if request.method=="POST":
        searched = request.POST['searched']
        note=models.notes.objects.filter(notes__contains=searched)
        return render(request,'notes/notes_search.html',{'searched':searched,'note':note})
    else:
        return render(request,'notes/notes_search.html',{})