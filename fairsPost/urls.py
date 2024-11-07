from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import post_home_view, add_fair_view, edit_fair_view, view_published_fairs, view_registered_fair, delete_selected_fair

app_name = 'post'

urlpatterns = [
    path('', post_home_view, name="post_home"),
    path("addfair", add_fair_view, name="add_fair"),
    path("editfair", edit_fair_view, name="edit_fair"),
    path("editfair/<int:feria_id>/", edit_fair_view, name="edit_selected_fair"),
    path("delete-fair/<int:feria_id>/", delete_selected_fair, name="delete_selected_fair"),
    path("my-fairs", view_published_fairs, name="view_published_fairs"),
    path("my-fair/<int:id>/", view_registered_fair, name="view_registered_fair")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
