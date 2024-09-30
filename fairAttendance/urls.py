from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import generateQR, readQR

urlpatterns = [
    path('successful-attendance/', readQR, name='successful_attendance'),
    path('successful-inscription/<int:registration_id>/<str:fair_title>/', generateQR, name='successful_inscription'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)