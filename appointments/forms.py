from pyexpat import model
from .models import Appointment
from django.forms import ModelForm

class AppointmentForm(ModelForm):
    class Meta:
        model=Appointment
        exclude = ('patient',)
        fields = '__all__'
            