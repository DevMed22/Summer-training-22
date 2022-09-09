from telnetlib import DO
from django.views.generic import ListView
from .models import Doctor


class DoctorsListView(ListView):
    model = Doctor
    context_object_name = 'doctors_list'
    template_name = 'doctors/doctors.html'