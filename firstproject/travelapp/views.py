from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import place,team,start

# Create your views here.
def demo(request):
    place1=place.objects.all()
    team1=team.objects.all()
    intro = start.objects.all()


    return render(request,'index.html',{'place1':place1,'team1':team1,'intro':intro})
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']
        if Password1==Password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Exists")
                return redirect('register')
            elif  User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else:
              user=User.objects.create_user(username=username,password=Password1,first_name=first_name,last_name=last_name,email=email)
              user.save()
              print("User created")
              return redirect('login')
        else:
            messages.info(request,"Passwords are not matching")
            return redirect('register')
        return redirect('/')

    return render(request,'registration.html')
def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid Credentials")
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
