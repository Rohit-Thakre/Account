from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from .models import User



# Create your views here.
def home(request):
    return render(request, 'base.html')


def login_method(request):

    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        email_check = User.objects.filter(email=email)
        if email_check:
            instance = authenticate(email=email, password=password)
            if instance:
                login(request, instance)
                return redirect('home')
            else:
                return render(request, 'login.html', {'val': True,  'msg': "Password Incorrect !"})

        else:
            return render(request, 'login.html', {'val': True,  'msg': "No account with this email"})

    return render(request, 'login.html', {'val': False})


def logout_method(request):
    logout(request)
    return redirect('home')


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


user_obj = None
def check_otp(request):
    otp_gen = 123

    if request.method == 'POST':

        email = request.POST.get('email')
        otp = request.POST.get('otp')

        global user_obj
        user_obj = User.objects.get(email = email)


        if  not user_obj: 
            return render(request, 'check_otp.html', {'val':True, 'msg':'Email does not exists!'})

        elif otp_gen == int(otp) : 
            return redirect('password_change')
        
        else: 
            return render(request, 'check_otp.html',{'val':True, 'msg':'Incorrect OTP!'} )

      
    return render(request,'check_otp.html')



def password_change_method(request):

    if request.method == 'POST':

        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            user_obj.set_password(pass1)
            user_obj.save()

            login(request,user_obj)

            return redirect('home')
        

    return render(request, 'password_reset.html')
