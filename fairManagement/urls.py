from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import register_fair, error_inscripcion

urlpatterns = [
    path('', register_fair, name='register_fair'),
    path('error-inscripcion/<str:message>/', error_inscripcion, name='error_inscripcion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)