from django.contrib import auth
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import record_table
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import add_record


# Create your views here.
def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
    return render(request, 'patients_record/index.html',{'user_status':username})


def about(request):
    return render(request,'patients_record/about.html')


def console(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        userpassword = request.POST['user_password']
        q = None
        user = authenticate(username=username, password=userpassword)
        if user is not None:
            login(request,user)
            q = record_table.objects.all().filter(physician_name = user)
            return render(request, 'patients_record/console.html',{'username':user,'userobject':q})
        else:
            return HttpResponse("Not found in user database")
    else:
        username = None
        if request.user.is_authenticated:
            username = request.user
            q = record_table.objects.all().filter(physician_name = username)
            return render(request, 'patients_record/console.html',{'username':username,'userobject':q})


def signin(request):
    return render(request, 'patients_record/signin.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_password2 = request.POST['user_password2']

        if user_password == user_password2:
            if User.objects.filter(username=user_name).exists() or User.objects.filter(email=user_email).exists():
                return HttpResponse("User name / Email taken already")
            else:
                user = User.objects.create_user(username=user_name,password=user_password,email=user_email)
                user.save();
                print("user created")
        else:
            return HttpResponse("Passwords didn't match :(")
                
    return redirect('/')

def add_record_to_table(request):
    if request.method == 'POST':
        doctor_form = add_record(request.POST)
        if doctor_form.is_valid():
            obj = doctor_form.save(commit=False)
            obj.slug = obj.patient_name +'-'+ obj.physician_name
            obj.save()
            return redirect("/")
        else:
            return HttpResponse("Invalid data")
    else:
        add_form = add_record()
        return render(request, 'patients_record/add_record.html',{'form':add_form})

def delete_record_from_table(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        date = request.POST['date_of_attendance']
        record_table.objects.filter(patient_name=patient_name, date_of_attendance=date).delete()
        return redirect('console')
    else:
        return render(request, "patients_record/delete_record.html")


def logging_in(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
    return render(request, 'patients_record/login.html',{'username':username})

def logging_out(request):
    logout(request)
    return redirect("/")