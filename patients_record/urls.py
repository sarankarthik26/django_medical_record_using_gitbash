from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('login/',views.logging_in,name="login"),
    path('contact/',views.contact,name="contact"),
    path('signin/',views.signin,name="signin"),
    path('console/',views.console,name="console"),
    path('register/',views.register,name="register"),
    path('logout/',views.logging_out,name="logout"),
    path('add_record/',views.add_record_to_table,name="add_record"),
    path('delete_record/',views.delete_record_from_table,name="delete_record"),
    path('adding_doctor/',views.add_doctor,name="add_doctor"),
    path('adding_patient/',views.add_patient,name="add_patient"),
    path('console/view_details/<int:key>/<str:pk>/',views.view_details,name="view_details"),
    #path('console/table/<slug:slug_holder>/',views.record),
]