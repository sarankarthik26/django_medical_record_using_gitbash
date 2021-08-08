from django.contrib import admin
from .models import record_table

class Admin_record_table(admin.ModelAdmin):
    list_display = ('patient_name','date_of_attendance','physician_name')
    list_filter = ('date_of_attendance','physician_name')
    prepopulated_fields = {'slug':('patient_name','physician_name')}
    search_fields = ('patient_name','date_of_attendance')


# Register your models here.
admin.site.register(record_table,Admin_record_table)
