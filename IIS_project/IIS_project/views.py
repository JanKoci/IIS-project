from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from appointments.models import Appointment
import datetime

class HomePage(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = Appointment
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'object_list': Appointment.objects.all().filter(appointment_date=datetime.date.today()).order_by('appointment_time')
        })
        return context
