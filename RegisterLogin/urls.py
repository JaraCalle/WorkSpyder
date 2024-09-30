from django.urls import path
from . import views
#Agregado pata el login
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

app_name = 'auth'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='view_fairs'), name='logout'),
   ]