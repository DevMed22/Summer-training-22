from .models import Appointment
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import AppointmentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User

class MakeAppointment(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/make_appointment.html'
    success_url = reverse_lazy('appointment_list')

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            self.model = form.save(commit=False)
            patient = User.objects.all()
            for username in patient:
                if str(self.request.user.username) == str(username):
                    self.model.patient = username
                    break
            self.model.save()
            return redirect('appointment_list')


class AppointmentDetail(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'


class AppointmentsList(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'


class DeleteAppointment(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_delete.html'
    success_url = reverse_lazy('home')


class UpdateAppointment(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_update.html'
    fields = ['date', 'phone', 'msg', 'department']
