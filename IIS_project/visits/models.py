from django.db import models
from django.urls import reverse
from patients.models import Patient

# Create your models here.

class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    visit_date = models.DateField(verbose_name="Date")
    visit_time = models.TimeField(verbose_name="Time")
    creation_date = models.DateField(auto_now_add=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Patient')

    def get_absolute_url(self):
        return reverse("visits:visit_detail", kwargs={'pk':self.pk})


class PerformanceBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        pass

class Performance(PerformanceBase):
    visit_id = models.ForeignKey(Visit, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("visits:visit_detail", kwargs={"pk" : self.visit_id.pk})

class Medicament(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    substance = models.CharField(max_length=50, blank=True)
    visit_id = models.ForeignKey(Visit, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("visits:visit_detail", kwargs={'pk':self.visit_id.pk})


# ExternalExamination ???
class Examination(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    workplace_city = models.CharField(max_length=50, blank=True)
    workplace_street = models.CharField(max_length=50, blank=True)
    workplace_postcode = models.CharField(max_length=5, blank=True)
    workplace_name = models.CharField(max_length=50)
    visit_id = models.ForeignKey(Visit, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("visits:visit_detail", kwargs={'pk':self.visit_id.pk})
