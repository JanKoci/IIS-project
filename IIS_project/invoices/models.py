from django.db import models
from patients.models import Patient 
from django.urls import reverse


# Create your models here.

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(verbose_name="Date")
    amount = models.IntegerField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Patient')

    def get_absolute_url(self):
        return reverse("invoices:invoice_detail", kwargs={"pk": self.pk})
    
    