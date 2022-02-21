from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User

# Create your views here.
def base(request):
    return render(request,'base.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is already taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password1)
                user.save()
                return redirect('login')
    else:
     return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user  = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('data')
        else:
            messages.info(request,'Invalid Email id and Password')
            return redirect('login')
    else:
     return render(request,'login.html')

def data(request):
    return render(request,'data.html')

