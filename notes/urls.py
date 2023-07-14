from django.urls import path
from .views import postnotes,notes,search_notes
app_name='notes'
urlpatterns=[
    path('notes/',postnotes,name="postnotes"),
    path('',notes,name="notes"),
    path('search_notes/',search_notes,name="search_notes")
]