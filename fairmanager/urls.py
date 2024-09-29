from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("addfair.html", views.addfair, name="addfair"),
    path("editfair.html", views.editfair, name="editfair"),
    path("editfair/<int:feria_id>/", views.editfair, name='editfair')
]