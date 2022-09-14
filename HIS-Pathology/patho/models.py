from django.db import models

# Create your models here.

class patient(models.Model):
    bill_no = models.IntegerField()
    case_id = models.IntegerField()
    reporting_date =models.DateField()
    patient_name = models.CharField(max_length=15)
    reference_doctor=models.CharField(max_length=15)
    amount=models.IntegerField()
    paid_amount=models.IntegerField()
    balance_amount=models.IntegerField()


    