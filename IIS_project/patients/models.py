from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


# Create your models here.

# Probably try to simplify it
class PhoneModel(models.Model):
    ...
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


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

    def get_absolute_url(self):
        return reverse("patients:patient_detail", kwargs={'pk':self.pk})



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


stat_id = 9707157835

from faker import Faker
def populate_users(num):
    global stat_id
    fake = Faker()
    for i in range(num):
        person_id = stat_id
        stat_id += 1
        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_date = fake.date(pattern="%Y-%m-%d", end_datetime=None)
        address_city = fake.city()
        address_street = fake.street_name()
        address_psc = fake.postcode()
        address_country = fake.country()
        phone_number = fake.phone_number()
        insurance = fake.company()
        p = Patient(person_id, first_name, last_name, birth_date, address_city,
            address_street, address_psc, address_country, phone_number)
        p.insurance = insurance
        p.save()
