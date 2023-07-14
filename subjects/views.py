from django.shortcuts import render , redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subject, SubjectCombination
from .forms import  SubjectCombinationForm, subjectform
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.views import View


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = subjectform
    
    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject Creation'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'Add Subject'
        return context

def subjectlistview(request):
    object_list = Subject.objects.all().values()
    template = loader.get_template('subjects/subject_list.html')
    context = {
        'object_list': object_list,
    }
    return HttpResponse(template.render(context, request))

# def SubjectCombinationListView(request):
#     #object_list = Subject.objects.all().values()
#     objec_list = SubjectCombination.objects.all().values()
#     #combined_queryset = zip(objec_list)
#     template = loader.get_template('subjects/subjectcombination_list.html')
#     context = {
#         'objec_list': objec_list,
#     }
#     return HttpResponse(template.render(context, request))
class SubjectCombinationListView(LoginRequiredMixin, ListView):
    model = SubjectCombination
    field_list = [
        'Class', 'Section', 'Subject'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage SubjectCombinations'
        context['panel_name']   =   'SubjectCombinations'
        context['panel_title']  =   'View SubjectCombinations Info'
        context['field_list']   =   self.field_list
        return context

class SubjectCombinationCreateView(LoginRequiredMixin, CreateView):
    model = SubjectCombination
    form_class = SubjectCombinationForm
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'SubjectCombination Creation'
        context['panel_name'] = 'SubjectConbinations'
        context['panel_title'] = 'Create SubjectConbination'
        return context

def SubjectDeleteView(pk):
    qs=Subject.objects.filter(subject_code = pk)
    Subject.delete(qs)
    return redirect ('subjects')
class SubjectCombinationDeleteView(LoginRequiredMixin, DeleteView):
    model = SubjectCombination
    template_name_suffix = "_delete"
    success_url = reverse_lazy('subjects:subject_combination_list')

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'SubjectCombination Delete Confirmation'
        context['panel_name'] = 'SubjectCombinations'
        context['panel_title'] = 'Delete SubjectCombination'
        return context

class SubjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Subject
    template_name_suffix = '_form'
    form_class = subjectform
    success_url = reverse_lazy('subjects:subject_list')

    
class SubjectCombinationUpdateView(LoginRequiredMixin, UpdateView):
    model = SubjectCombination
    template_name_suffix = '_form'
    form_class = SubjectCombinationForm
    success_url = reverse_lazy('subjects:subject_combination_list')