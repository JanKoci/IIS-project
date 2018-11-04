import django_filters
from models import Patient

class PatientFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Patient
        fields = ['person_id', 'first_name', 'last_name', 'birth_date',]
