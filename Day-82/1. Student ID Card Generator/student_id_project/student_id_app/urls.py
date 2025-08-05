from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_id_app.urls')),  # ✅ include your app, NOT the project
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_student, name='upload_student'),
    path('list/', views.list_students, name='list_students'),
]