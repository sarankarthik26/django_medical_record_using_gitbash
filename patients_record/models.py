from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from django.urls import reverse


gender = (('m','Male'),('f','Female'),('e','Does not want to mention'))

# Create your models here.

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)
    patient_age = models.PositiveIntegerField()
    patient_gender = models.CharField(choices=gender,max_length=10)
    patient_bloodgroup = models.CharField(max_length=6)
    patient_phone_number = models.CharField(max_length=12)
    patient_address = models.TextField()

    def __str__(self):
        return f'{self.patient_name}-{self.user.email}'

class DoctorProfile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=50)
    doctor_age = models.PositiveIntegerField()
    doctor_gender = models.CharField(choices=gender,max_length=10)
    doctor_designation = models.CharField(max_length=50)
    doctor_phone_number = models.CharField(max_length=12)
    doctor_address = models.TextField()

    def __str__(self):
        return f'{self.doctor_name}-{self.user.email}'

class record_table(models.Model):
    patient = models.ForeignKey(PatientProfile,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile,on_delete=PROTECT)
    is_allergic = models.BooleanField()
    patient_description_file = models.TextField()
    date_of_attendance = models.DateField()
    time_of_attendance = models.TimeField()

    def __str__(self):
        return f'{self.patient.patient_name}:{self.doctor.doctor_name}:{self.date_of_attendance}'

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])