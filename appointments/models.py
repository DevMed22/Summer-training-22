from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):
    date = models.DateField()
    phone = models.CharField(max_length=12)
    msg = models.CharField(max_length=150, null=True, blank=True)
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    DEPARTMENTS = [
        ('General Health', 'General Health'),
        ('Cardiology', 'Cardiology'),
        ('Dental', 'Dental'),
    ]
    department = models.CharField(max_length=15, choices=DEPARTMENTS)

    def __str__(self):
        return self.patient.username

    def get_absolute_url(self):
        return reverse('appointment_detail', kwargs={'pk': self.pk})
