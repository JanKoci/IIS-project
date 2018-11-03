from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

# Probably try to simplify it
class PhoneModel(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list


class Patient(models.Model):
    person_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField()
    address_city = models.CharField(max_length=50)
    address_street = models.CharField(max_length=50)
    address_psc = models.CharField(max_length=5)
    address_country = models.CharField(max_length=50)
    phone_number = PhoneModel()
    insurance = models.CharField(max_length=50)


class RegisteredPatient(models.Model):
    person_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    registration_date = models.DateField()


class NotRegisteredPatient(models.Model):
    person_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor_first_name = models.CharField(max_length=25)
    doctor_last_name = models.CharField(max_length=25)
    doctor_phone = PhoneModel()
    doctor_address_city = models.CharField(max_length=50)
    doctor_address_street = models.CharField(max_length=50)
    doctor_address_psc = models.CharField(max_length=5)
    doctor_address_country = models.CharField(max_length=50)
