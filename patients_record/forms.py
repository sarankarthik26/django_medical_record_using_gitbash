from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import record_table, PatientProfile, DoctorProfile
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class add_record(ModelForm):
    class Meta:
        model = record_table
        fields = ['patient', 'doctor','is_allergic','patient_description_file','date_of_attendance','time_of_attendance']
        widgets = {
            'date_of_attendance': DateInput(),
            'time_of_attendance': TimeInput()
        }

class doctor_form(ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['doctor_name','doctor_age', 'doctor_gender', 'doctor_designation', 'doctor_phone_number', 'doctor_address']

class patient_form(ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['patient_name','patient_age','patient_gender','patient_bloodgroup','patient_phone_number','patient_address']

class delete_record_form(ModelForm):
    class Meta:
        model = record_table
        fields = ['patient', 'doctor', 'date_of_attendance']
        widgets = {
            'date_of_attendance':DateInput()
        }