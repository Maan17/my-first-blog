from django.shortcuts import render,redirect     
from django.contrib import messages
from django.contrib.auth.models import User,auth

def login(request):
    if request.method=='POST':
        username=reuquest.POST['username']
        password=request.POST['password']

        user.auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")

        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return redirect(request,"blog/login.html")

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','NULL')
        last_name=request.POST.get('last_name','NULL')
        username=request.POST.get('username','NULL')
        password1=request.POST.get('password1','NULL')
        password2=request.POST.get('password2','NULL')
        email=request.POST.get('email','NULL')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already registered')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("User created")
                return redirect('login')

        else:
            messages.info(request,"Password don't match!")
            return redirect('register')
    else:
        return render(request,"blog/register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")