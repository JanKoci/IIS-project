from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


# Create your models here.

# make them local variables ?
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed")
id_regex = RegexValidator(regex=r'^[0-9]+$', message="Id should contain only numbers")
psc_regex = RegexValidator(regex=r'^[0-9]{5}', message="Postcode has to be 5 digit number")


class Patient(models.Model):
    global phone_regex
    person_id = models.CharField(max_length=10, primary_key=True, validators=[id_regex])
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField()
    address_city = models.CharField(max_length=50)
    address_street = models.CharField(max_length=50)
    address_psc = models.CharField(max_length=5, validators=[psc_regex])
    address_country = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    insurance = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("patients:patient_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return "{first_name} {last_name} ( {person_id} )".format(
                                                            first_name=self.first_name,
                                                            last_name=self.last_name,
                                                            person_id=self.person_id
                                                        )



class RegisteredPatient(Patient):
    registration_date = models.DateField(auto_now_add=True)


class NotRegisteredPatient(Patient):
    global phone_regex
    doctor_first_name = models.CharField(max_length=25)
    doctor_last_name = models.CharField(max_length=25)
    doctor_phone = models.CharField(validators=[phone_regex], max_length=17)
    doctor_address_city = models.CharField(max_length=50)
    doctor_address_street = models.CharField(max_length=50)
    doctor_address_psc = models.CharField(max_length=5, validators=[psc_regex])
    doctor_address_country = models.CharField(max_length=50)


stat_id = 9707157835

from faker import Faker
def populate_users(num):
    global stat_id
    fake = Faker()
    not_registered_ratio = 0.3

    not_registered = round(num * not_registered_ratio)
    registered = num - not_registered

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
        p = RegisteredPatient(person_id, first_name, last_name, birth_date, address_city,
            address_street, address_psc, address_country, phone_number, insurance)
        p.insurance = insurance
        p.registration_date = fake.date(pattern="%Y-%m-%d", end_datetime=None)
        p.save()

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
        p = NotRegisteredPatient(person_id, first_name, last_name, birth_date, address_city,
            address_street, address_psc, address_country, phone_number, insurance)
        # p.insurance = insurance
        p.doctor_first_name = fake.first_name()
        p.doctor_last_name = fake.last_name()
        p.doctor_phone = fake.phone_number()
        p.doctor_city = fake.city()
        p.doctor_street = fake.street_name()
        p.doctor_psc = fake.postcode()
        p.doctor_country = fake.country()
        p.save()
