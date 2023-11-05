from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_method, name='login_methon'),

]