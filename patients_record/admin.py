from django.contrib import admin
from .models import record_table, DoctorProfile, PatientProfile

class Admin_record_table(admin.ModelAdmin):
    list_display = ('patient','date_of_attendance','doctor')
    list_filter = ('patient','date_of_attendance','doctor')
    search_fields = ('patient','date_of_attendance','doctor')

class User_record_table(admin.ModelAdmin):
    list_display = ('patient_name','patient_age','patient_phone_number')
    list_filter = ('patient_name','patient_phone_number')
    search_fields = ('patient_name','patient_phone_number')

class Doctor_record_table(admin.ModelAdmin):
    list_display = ('doctor_name','doctor_designation','doctor_phone_number')
    list_filter = ('doctor_name','doctor_phone_number','doctor_designation')
    search_fields = ('doctor_name','doctor_phone_number')


# Register your models here.
admin.site.register(record_table,Admin_record_table)
admin.site.register(PatientProfile,User_record_table)
admin.site.register(DoctorProfile, Doctor_record_table)