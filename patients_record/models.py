from django.db import models
from django.db.models.fields import SlugField


gender = (('m','Male'),('f','Female'),('e','Does not want to mention'))

# Create your models here.

class record_table(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_age = models.PositiveIntegerField()
    patient_gender = models.CharField(choices=gender,max_length=10)
    physician_name = models.CharField(max_length=50)
    date_of_attendance = models.DateField()
    slug = SlugField(unique=True)
    patient_address = models.TextField()
    patient_phone_number = models.CharField(max_length=12)
    is_allergic = models.BooleanField()
    patient_description_file = models.TextField()

    def __str__(self):
        return f'{self.patient_name}-{self.physician_name}'

