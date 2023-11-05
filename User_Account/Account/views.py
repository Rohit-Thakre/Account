from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')


def login_method(request):
    return render(request, 'login.html')


def register_method(request):

    if request.method == 'POST': 
        return redirect('home')
    return render(request, 'register.html')

def password_change_method(request):
    return render(request, 'password_reset.html')