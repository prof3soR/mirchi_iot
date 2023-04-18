from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def user_profile(request):
    return render(request,"user_profile.html")
def login_view(request):
    if request.method == "POST":
        username = request.POST["mobile"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.add_message(request, messages.SUCCESS, 'Login successfull!')
            return render(request,"service_request.html")
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials!')
            return render(request,"login.html",)
    else:
        return render(request,"login.html")
        

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logged out!')
    return render(request,"login.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('mobile')
        email=request.POST.get("email")
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        dp=request.POST.get("dp")

        # Check if the username is available
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, 'This mobile number is already exits! Try loging in.')
            return render(request, 'signup.html')

        # Create the new user object
        user = User.objects.create_user(username=username, password=password, first_name=first_name, email=email)
        user.save()
        new_customer=customer(user=user,dp=dp)
        new_customer.save()
        messages.add_message(request, messages.SUCCESS, 'Account created! Please login')
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'signup.html')


def mechanic_registration(request):
    if request.method == 'POST':
        username = request.POST.get('mobile')
        alt_mobile = request.POST.get('alt_mobile')
        email=request.POST.get("email")
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        dp=request.POST.get("image")
        shop_dp=request.POST.get("shop_image")
        address=request.POST.get("Address")
        car_company=request.POST.get("car_company")
        # Check if the username is available
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, 'This mobile number is already exits! Try loging in.')
            return render(request, 'mechanic_signup.html')

        # Create the new user object
        user = User.objects.create_user(username=username, password=password, first_name=first_name, email=email)
        user.save()
        new_mech=mechanic(user=user,alt_mobile=alt_mobile,dp=dp,shop_dp=shop_dp,address=address,car_company=car_company)
        new_mech.save()
        messages.add_message(request, messages.SUCCESS, 'Account created! Please login')
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'mechanic_signup.html')

def dashboard(request):
    #user=request.user
    near_mech=mechanic.objects.all()
    #if requests==None or requests.request_status==True:
        #return render(request,"dashboard.html",{"message":"you have no open service request!"})
    #near_mech=mechanic.objects.filter(address=requests.Address)
    return render(request,"dashboard.html",{"near_mechs":near_mech})
    

    

from datetime import datetime

def srequest(request):
    if request.method=="POST":
        car_company=request.POST.get("car_company")
        latitude=request.POST.get("lat")
        longitude=request.POST.get("log")
        location=request.POST.get("Address")
        user=request.user
        mobile=request.POST.get("mobile")
        new_request=service_Request(user=user,
                                    Address=location,
                                    lat=latitude,
                                    log=longitude,
                                    contact=mobile,
                                    car_company=car_company,
                                    dateandtime=datetime.now())
        new_request.save()
        return HttpResponseRedirect("dashboard")
    else:
        return render(request,"service_request.html")


def request_details_user(request,mech):
    mech
    
