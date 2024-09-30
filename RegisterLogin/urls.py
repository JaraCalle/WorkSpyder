#Agregado pata el login
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='RegisterLogin/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='RegisterLogin/logout.html'), name='logout'),
   ]