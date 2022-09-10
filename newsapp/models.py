from email.policy import default
from pyexpat import model
from re import T
from tkinter.tix import Tree
from django.db import models
from doctors.models import Doctor
from django.urls import reverse
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pic = models.ImageField(default='news-image.jpg')
    newsdate = models.DateField(auto_now_add=True, null=True, blank=True)
    docname = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('new_detail', kwargs={'pk': self.pk})
