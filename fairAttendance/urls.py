from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import generateQR, readQR, google_calendar_init, schedule_fair

urlpatterns = [
    path('read-attendance/<int:qr_id>', readQR, name='successful_attendance'),
    path('successful-inscription/<int:registration_id>/<str:fair_title>/', generateQR, name='successful_inscription'),
    path('schedule-fair/<int:registration_id>/', schedule_fair, name='schedule_fair'),
    path('google-calendar/init/', google_calendar_init, name='google_calendar_init'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)