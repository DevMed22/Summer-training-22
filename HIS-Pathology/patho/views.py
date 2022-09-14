from django.views.generic import ListView ,TemplateView

from patho.models import patient


class HomePageView(TemplateView):
    template_name = 'home.html'

class PathoView(ListView):
    model =patient
    template_name='patho/pathology.html'