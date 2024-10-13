from django.urls import path
from .views import view_profile, edit_profile

app_name = 'profile'

urlpatterns = [
    path('', view_profile, name="view_profile"),
    path('edit', edit_profile, name="edit_profile"),
   ]