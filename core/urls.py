from django.urls import path
from . import views
from django.contrib.auth import views as auht_views
urlpatterns=[
    path('',views.frontpage, name="frontpage"),
    path('signup/',views.signup, name= "signup"),
    path('login/', auht_views.LoginView.as_view(template_name='core/login.html'),name="login"),
    path('logout/',auht_views.LogoutView.as_view(), name='logout')
]