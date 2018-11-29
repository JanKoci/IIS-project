from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    
    template_name = 'home_page.html'
