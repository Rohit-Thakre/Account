from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_method, name='login'),
    path('register/', views.register_method, name='register'),
    path('password_change/', views.password_change_method, name='password_change'),


]