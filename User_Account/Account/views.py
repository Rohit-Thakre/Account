from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .models import User



# Create your views here.
def home(request):
    return render(request, 'base.html')


def login_method(request):
    return render(request, 'login.html')


def register_method(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        try:
            usr_obj = User.objects.get(email = email)

            if usr_obj: 
                print('email taken')
                return render(request, 'register.html', {'val': True, 'msg': 'Email Taken !'})
        

        except:
            user_obj = User.objects.create(full_name=full_name, email=email, username = full_name+'+'+email)
            user_obj.set_password(pass1)
            user_obj.save()
            login(request, user_obj)
            return redirect('home')


    return render(request, 'register.html')

def password_change_method(request):
    return render(request, 'password_reset.html')



