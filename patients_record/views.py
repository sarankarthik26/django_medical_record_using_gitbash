from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import record_table, DoctorProfile, PatientProfile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import add_record, doctor_form, patient_form, delete_record_form
from django.contrib.auth.decorators import login_required
import re


# Create your views here.
def index(request):
    username = None
    num_visits = 0
    if request.user.is_authenticated:
        username = request.user
        num_visits = request.session.get('num_visits', 1)
        request.session['num_visits'] = num_visits + 1
    return render(request, 'patients_record/index.html',{'user_status':username,'visits':num_visits})


def about(request):
    return render(request,'patients_record/about.html')

def console(request):
    if request.method == 'POST':

        try:
            search_name = request.POST['search_patient']
            user = request.user
            pre_email = User.objects.get(username=user).email
            q = record_table.objects.filter(doctor__user__email=pre_email,patient__patient_name__icontains = search_name).order_by('-date_of_attendance')
            return render(request, 'patients_record/console.html',{'username':user,'userobject':q,'bool':False})

        except:
            try:
                search_name = request.POST['search_doctor']
                user = request.user
                pre_email = User.objects.get(username=user).email
                q = record_table.objects.filter(patient__user__email=pre_email,doctor__doctor_name__icontains = search_name).order_by('-date_of_attendance')
                return render(request, 'patients_record/console.html',{'username':user,'userobject':q,'bool':True})
            except:
                username = request.POST['user_name']
                userpassword = request.POST['user_password']
                q = None
                user = authenticate(username=username, password=userpassword)
                if user is not None:
                    login(request,user)
                else:
                    return HttpResponse("Not found in user database")
    else:
        user = None
        if request.user.is_authenticated:
            user = request.user
        else:
            return HttpResponse("User not logged in :(")

    pre_email = User.objects.get(username=user).email
    reg_email = re.search(r'@test.com',pre_email)
    val = False
    if reg_email:
        q = record_table.objects.filter(doctor__user__email=pre_email).order_by('-date_of_attendance')
    elif re.search(r'@admin.com',pre_email):
        q = record_table.objects.all().order_by('-date_of_attendance')
    else:
        q = record_table.objects.filter(patient__user__email=pre_email).order_by('-date_of_attendance')
        val = True
    return render(request, 'patients_record/console.html',{'username':user,'userobject':q,'bool':val})


def signin(request):
    return render(request, 'patients_record/signin.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_password2 = request.POST['user_password2']
        try:
            checkval = request.POST['check']
            checkval = True
        except:
            checkval = False

        if user_password == user_password2:
            if User.objects.filter(username=user_name).exists() or User.objects.filter(email=user_email).exists():
                return HttpResponse("User name / Email taken already")
            else:
                user = User.objects.create_user(username=user_name,password=user_password,email=user_email)
                user.save();
                print("user created")
                userval = authenticate(username=user_name, password=user_password)
                login(request,userval)
                if not checkval:
                    return render(request,'patients_record/customer_details.html', {'form':patient_form})
                else:
                    return render(request,'patients_record/doctor_details.html',{'form':doctor_form})
        else:
            return HttpResponse("Passwords didn't match :(")
                
    return redirect('/')

@login_required(login_url='/login/')
def add_record_to_table(request):
    if request.method == 'POST':
        doctor_form = add_record(request.POST)
        if doctor_form.is_valid():
            obj = doctor_form.save()
            return redirect("/console/")
        else:
            return HttpResponse("Invalid data")
    else:
        add_form = add_record()
        return render(request, 'patients_record/add_record.html',{'form':add_form})

@login_required(login_url='/login/')
def delete_record_from_table(request):
    if request.method == 'POST':
        delete_form = delete_record_form(request.POST)
        if delete_form.is_valid():
            name_of_patient = delete_form.cleaned_data.get("patient")
            name_of_doctor = delete_form.cleaned_data.get("doctor")
            date_from_form = delete_form.cleaned_data.get("date_of_attendance")
        
        record_table.objects.filter(patient=name_of_patient, doctor = name_of_doctor,date_of_attendance=date_from_form).delete()
        return redirect('console')
    else:
        pass_form = delete_record_form()
        return render(request, "patients_record/delete_record.html",{'form':pass_form})

def add_doctor(request):
    if request.method == 'POST':
        doctor_data = doctor_form(request.POST)
        if doctor_data.is_valid():
            obj = doctor_data.save(commit=False)
            print("OBJ-->sdf")
            obj.user = User.objects.get(username=request.user.username)
            obj.save()
        else:
            return HttpResponse("invalid data")
    return redirect('/')

def add_patient(request):
    if request.method == 'POST':
        patient_data = patient_form(request.POST)
        if patient_data.is_valid():
            obj = patient_data.save(commit=False)
            obj.user = User.objects.get(username=request.user.username)
            obj.save()
        else:
            return HttpResponse("invalid data")
    return redirect('/')

@login_required(login_url='/login/')
def view_details(request, key, pk):
    if key==1:
        q = DoctorProfile.objects.get(user__username=pk)
        col = DoctorProfile._meta.get_fields()
    elif key==0:
        q = PatientProfile.objects.get(user__username=pk)
        col = PatientProfile._meta.get_fields()
    else:
        vals = pk.split(':')
        q = record_table.objects.get(patient__patient_name=vals[0], doctor__doctor_name = vals[1], date_of_attendance=vals[2])
        col = record_table._meta.get_fields()
    return render(request, 'patients_record/display_profile.html',{'obj':q,'col':col,'key':key})


def logging_in(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
    return render(request, 'patients_record/login.html',{'username':username})

def logging_out(request):
    logout(request)
    return redirect("/")