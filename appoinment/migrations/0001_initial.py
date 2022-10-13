# Generated by Django 4.1.1 on 2022-09-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_Name', models.CharField(max_length=120, unique=True)),
                ('Patient_Name', models.CharField(max_length=120, unique=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
            ],
        ),
    ]