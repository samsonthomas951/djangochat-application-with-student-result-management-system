from django.shortcuts import render , redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from student_classes.models import StudentClass

def StudentCreateView(request):
    if request.method =="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            
    else:
        form = StudentForm()
    return render(request,'students/student_form.html',{'form':form,})

def StudentListView(request):
    object_list = Student.objects.all().values()
    template = loader.get_template('students/student_list.html')
    context = {
        'object_list': object_list,
    }
    return HttpResponse(template.render(context, request))    


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name_suffix = '_form'
    form_class = StudentForm
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Update Student Info'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Update Student info'
        return context

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name_suffix = '_delete'
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Student Delete Confirmation'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Delete Student'
        return context
