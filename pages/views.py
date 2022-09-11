from django.views.generic import TemplateView
from doctors.models import Doctor


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self):
        context = Doctor.objects.all()
        return {'doctors': context, }


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
