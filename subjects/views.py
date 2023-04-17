from django.shortcuts import render , redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subject, SubjectCombination
from .forms import  SubjectCombinationForm, subjectform
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.views import View
# Create your views here.


def SubjectForm(request):
    if request.method =="POST":
        form=subjectform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = subjectform
    return render(request,'subjects/subject_form.html',{'form':form})

def subjectlistview(request):
    object_list = Subject.objects.all().values()
    template = loader.get_template('subjects/subject_list.html')
    context = {
        'object_list': object_list,
    }
    return HttpResponse(template.render(context, request))

def SubjectCombinationListView(request):
    object_list = Subject.objects.all().values()
    template = loader.get_template('subjects/subjectcombination_list.html')
    context = {
        'object_list': object_list,
    }
    return HttpResponse(template.render(context, request))

def SubjectCombinationform(request):
    if request.method == 'POST':
        form = SubjectCombinationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=SubjectCombinationForm
    return render(request,'subjects/subjectcombination_form.html',{'form':form})

def SubjectDeleteView(pk):
    qs=Subject.objects.filter(subject_code = pk)
    Subject.delete(qs)
    return redirect ('subjects')
def SubjectCombinationDeleteView(pk):
    qs = SubjectCombination.objects.filter(id=pk)
    Subject.delete(qs)
    return redirect('subjects')

def SubjectCombinationUpdateView(request):
    if request == 'POST':
        form = SubjectCombinationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=SubjectCombinationForm
    return render(request,'subjects/subjectcombination_form.html',{'form':form})