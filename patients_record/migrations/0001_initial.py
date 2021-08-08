# Generated by Django 3.2.6 on 2021-08-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('patient_age', models.PositiveIntegerField()),
                ('patient_gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('e', 'Does not want to mention')], max_length=10)),
                ('physician_name', models.CharField(max_length=50)),
                ('date_of_attendance', models.DateField()),
                ('slug', models.SlugField(unique=True)),
                ('patient_address', models.TextField()),
                ('patient_phone_number', models.CharField(max_length=12)),
                ('is_allergic', models.BooleanField()),
                ('patient_description_file', models.TextField()),
            ],
        ),
    ]