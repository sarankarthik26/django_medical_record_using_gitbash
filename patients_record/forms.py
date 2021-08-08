from django.db.models import fields
from django.forms import ModelForm
from .models import record_table

class add_record(ModelForm):
    class Meta:
        model = record_table
        fields = ['patient_name', 'patient_age', 'patient_gender','physician_name','date_of_attendance','patient_address','patient_phone_number','is_allergic','patient_description_file']