from django.urls import path
from .views import ( SubjectForm, subjectlistview,SubjectDeleteView,SubjectCombinationListView,SubjectCombinationform,SubjectCombinationUpdateView,SubjectCombinationDeleteView)


app_name = 'subjects'

urlpatterns = [
    path('', subjectlistview, name='subject_list'),
    path('create/', SubjectForm, name='create_subject'),
    path('update/<int:pk>/', SubjectForm, name='update_subject'),
    path('delete/<int:pk>/', SubjectDeleteView, name='delete_subject'),

    # SubjectConbinations
    path('combination/create/', SubjectCombinationform, name='create_subject_combination'),
    path('combination/list/', SubjectCombinationListView, name='subject_combination_list'),
    path('combination/update/<int:pk>', SubjectCombinationUpdateView, name='subject_combination_update'),
    path('combination/delete/<int:pk>', SubjectCombinationDeleteView, name='subject_combination_delete' ),
]