from django.shortcuts import render, redirect
from .forms import NotesForm
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import models
def postnotes(request):
    if request.method =="POST":
        #notes=request.POST.get('notes_title')
        form=NotesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # subject = f'Hi, new  notes have been post'
            # message = f'Visit https:/localhost:8000/notes to check them out'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = ['samsonthomas951@gmail.com']
            # send_mail( subject, message, email_from, recipient_list)
            return redirect("/")
    else:
        form = NotesForm()
    return render(request,'notes/notes_form.html',{'form':form,})
def notes(request):
    Notes = models.notes.objects.all().values()
    template = loader.get_template('notes/notes.html')
    context = {
    'Notes': Notes
    }
    return HttpResponse(template.render(context, request))


