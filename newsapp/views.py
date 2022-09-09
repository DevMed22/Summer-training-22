from django.views.generic import ListView, DetailView

from .models import News


class NewPageView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'newsapp/news_list.html'


class NewDetailView(DetailView):
    model = News
    template_name = 'newsapp/new_detail.html'
