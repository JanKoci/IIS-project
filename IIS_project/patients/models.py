"""
    TODO:
        * validators
            - aby nebylo birth_date v budoucnosti
"""

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
    address_city = models.CharField(max_length=50, blank=True)
    address_street = models.CharField(max_length=50, blank=True)
    address_psc = models.CharField(max_length=5, validators=[psc_regex], blank=True)
    address_country = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    insurance = models.CharField(max_length=50, blank=True)

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
    doctor_first_name = models.CharField(max_length=25, blank=True)
    doctor_last_name = models.CharField(max_length=25, blank=True)
    doctor_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    doctor_address_city = models.CharField(max_length=50, blank=True)
    doctor_address_street = models.CharField(max_length=50, blank=True)
    doctor_address_psc = models.CharField(max_length=5, validators=[psc_regex], blank=True)
    doctor_address_country = models.CharField(max_length=50, blank=True)

