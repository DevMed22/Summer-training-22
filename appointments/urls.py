from django.urls import path
from .views import MakeAppointment, AppointmentsList, AppointmentDetail, DeleteAppointment, UpdateAppointment

urlpatterns = [
    path('', AppointmentsList.as_view(), name='appointment_list'),
    path('create/', MakeAppointment.as_view(), name='makeappointment'),
    path('<int:pk>/', AppointmentDetail.as_view(),
         name='appointment_detail'),
    path('<int:pk>/delete/', DeleteAppointment.as_view(),
         name='appointment_delete'),
    path('<int:pk>/update/', UpdateAppointment.as_view(),
         name='appointment_update'),

]
