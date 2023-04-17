
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('' ,include('core.urls')),
    path('admin/', admin.site.urls),
    path('rooms/', include('room.urls')),
    path('subjects/', include('subjects.urls')),
    path('students/', include('students.urls')),
    path('classes/', include('student_classes.urls')),
    path('results/', include('results.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('postnotes/',include('notes.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
