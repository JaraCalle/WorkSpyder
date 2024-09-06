from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import view_fairs, fair_detail_view

urlpatterns = [
    path('', view_fairs, name='view_fairs'),
    path('fair/<int:id>/', fair_detail_view, name='fair'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
