from django.forms import ModelForm
from patients import models

class RegPatientForm(ModelForm):
    class Meta:
        model = models.RegisteredPatient
        fields = ['first_name', 'last_name', 'person_id', 'birth_date', 'address_city',
                'address_street', 'address_psc', 'address_country', 'phone_number',
                'insurance']

class NotRegPatientForm(ModelForm):
    class Meta:
        model = models.NotRegisteredPatient
        fields = ['first_name', 'last_name', 'person_id', 'birth_date', 'address_city',
                'address_street', 'address_psc', 'address_country', 'phone_number',
                'insurance', 'doctor_first_name', 'doctor_last_name', 'doctor_phone',
                'doctor_address_city', 'doctor_address_street', 'doctor_address_psc',
                'doctor_address_country']
