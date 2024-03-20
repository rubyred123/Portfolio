import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# Create your views here.
def signup(request):

    if request.method == "POST":
        get_email = request.POST.get("email")
        get_password = request.POST.get("password1")
        get_conf_password = request.POST.get("password2")
        
        if get_password != get_conf_password:
            messages.info(request,"Password is not matching")
            return redirect('/auth/signup')
        
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"Email is already registered")
                return redirect('/auth/signup')

        except Exception as identifier:
            pass

        myUser =  User.objects.create_user(get_email, get_email, get_password)
        myUser.save()
        messages.success(request, "User is created, Please login")
        return redirect('/auth/login')
    return render(request,'signup.html')



def login(request):

     if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        
        myuser = authenticate(username=email, password=pass1)

        if myuser is not None:
            auth_login(request, myuser)
            #messages.success(request,"Login Successful")
            return redirect("/")

        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/auth/login")
        
     return render(request,'login.html')



def logout(request):

    auth_logout(request)
    messages.success(request,"Logout success")

    return render(request,'login.html')