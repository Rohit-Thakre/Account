from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')


def login_method(request):
    return render(request, 'login.html')


def register_method(request):
    return render(request, 'register.html')

def password_change_method(request):
    return render(request, 'password_reset.html')