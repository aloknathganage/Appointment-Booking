from django.shortcuts import render , redirect
from email import message
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import auth 
from django.contrib.auth.decorators import login_required
from .models import Appoinments,Registerd
from django.contrib import messages 
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def index2(request):
    return render(request,'index2.html')

def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password1 = request.POST['password1']
        user = authenticate(request, email=email, password1=password1)
        if request.user.is_authenticated:
            auth.login(request, user)
            return redirect('index2')
        else:
            messages.error(request, "Your login credentials is not match")
            return render(request,'login.html')    
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('index.html')
    else:
        return render(request, 'login.html')


# def contact(request):
#     if request.method == 'POST':
#         Name = request.POST.get('Name','')
#         Phone = request.POST.get('Phone','')
#         Email = request.POST.get('Email','')
#         Message = request.POST.get('Message','')
#         order = Connections(Name=Name,Phone=Phone ,Message=Message, Email=Email)
#         order.save()
#         return redirect('/')
#     else:
#         return render(request,'contact.html')


def signup(request):
    print('before if')
    if request.method=="POST":
        # Get the post parameters
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        # lname=request.POST.get('lname','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')
        print('after if')
        if password1==password2:
            user = Registerd(name=name,email=email,password1=password1,password2=password2)
            user.save()
            print('after save ')
            messages.success(request, "Your Account Has Been Created")
            return redirect("login")           
        else:
            return redirect('/')
    
    return render(request,"signup.html")

@login_required(login_url='/login')
def appoinment(request):
    if request.method=='POST':
        Name = request.POST.get('Name','')
        Age = request.POST.get('Age','')
        Gender = request.POST.get('Gender','')
        Phone = request.POST.get('Phone','')
        DateTime = request.POST.get('DateTime','')
        Message = request.POST.get('Message','')
        error_message=None
        
        if not error_message:
            order=Appoinments(Name=Name, Age=Age, Gender=Gender, Phone=Phone ,Message=Message, DateTime= DateTime)
            order.save()
            # messages.success(request, "your appointment is successfully fixed")
            return render(request,'index2.html')
        else:
            return redirect('appoinment',{'error':error_message})
    else:
        return render(request,'appoinment.html')


