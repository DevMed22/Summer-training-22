from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from doctors.models import Doctor

from .models import News
from .forms import CreateStory

from django.views import View

class NewPageView(ListView):
    model = News
    template_name = 'newsapp/news_list.html'
    
    def get_context_data(self,**kwargs):
        context = Doctor.objects.all()
        news = News.objects.all()
        return {'doctors':context, 'news_list':news}
    


class NewDetailView(DetailView):
    model = News
    template_name = 'newsapp/new_detail.html'





class StoryCreate(CreateView):
    model = News
    form_class = CreateStory
    template_name = 'newsapp/create_story.html'
    success_url = reverse_lazy("news")
    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            self.model = form.save(commit=False)
            doc = Doctor.objects.all()
            for username in doc:
                if str(self.request.user.username) == str(username):
                    self.model.docname = username
                    break
            self.model.save()
            return redirect('news')