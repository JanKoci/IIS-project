from django.contrib import admin
from visits.models import Visit, Examination, Medicament, Performance

# Register your models here.
admin.site.register(Visit)
admin.site.register(Examination)
admin.site.register(Medicament)
admin.site.register(Performance)
