from django.urls import path
from .views import DoctorsListView

urlpatterns = [
    path('', DoctorsListView.as_view(), name='doctors_list'),
]