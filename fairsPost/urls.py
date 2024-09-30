from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import post_home_view, add_fair_view, edit_fair_view

urlpatterns = [
    path('', post_home_view, name="post_home"),
    path("addfair", add_fair_view, name="add_fair"),
    path("editfair", edit_fair_view, name="edit_fair"),
    path("editfair/<int:feria_id>/", edit_fair_view, name="edit_selected_fair")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
