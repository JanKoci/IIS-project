from django import forms
from visits.models import Visit

class VisitCreateForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['visit_date', 'patient_id']
        widgets = {
            'patient_id' : forms.TextInput(),
        }
