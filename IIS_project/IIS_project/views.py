from django.views.generic import ListView
from appointments.models import Appointment
import datetime

class HomePage(ListView):
    model = Appointment
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'object_list': Appointment.objects.all().filter(appointment_date=datetime.date.today())
        })
        return context
    