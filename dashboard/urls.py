from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('', views.find_result_view, name='find_result'),
    path('change-password/', views.PasswordChangeView.as_view(), name='change_password'),
    path('find-result/<int:pk>/result/', views.result, name='get_result'),
    path('print_pdf/<int:id>/', views.pdf.as_view(), name='save_as_pdf'),
]