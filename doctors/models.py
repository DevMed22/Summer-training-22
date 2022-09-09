from django.db import models

"""
class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField()
    CHOICES = [
        ('General Health', 'General Health'),
        ('Cardiology', 'Cardiology'),
        ('Dental', 'Dental'),
        ('Medical Research', 'Medical Research'),
    ]
    department = models.CharField(max_length=150, choices=CHOICES)
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=100, null=True, blank=True)
"""


class Doctor(models.Model):
    # username
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    title = models.CharField(max_length=150)
    linkedin = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=12)
    DEPARTMENTS = [
        ('General Health', 'General Health'),
        ('Cardiology', 'Cardiology'),
        ('Dental', 'Dental'),
        ('Medical Research', 'Medical Research')
    ]
    department = models.CharField(max_length=150, choices=DEPARTMENTS)

    doc_pic = models.ImageField(default=None)

    # appointments = models.ForeignKey(
    #    Appointment, on_delete=models.PROTECT
    # )

    def __str__(self):
        return self.name
