from django.urls import path
from .views import postnotes,notes
app_name='notes'
urlpatterns=[
    path('postnotes/',postnotes,name="postnotes"),
    path('',notes,name="notes")
]