from django.urls import path
from .views import NewPageView, NewDetailView,  StoryCreate


urlpatterns = [
    
    path('', NewPageView.as_view(), name='news'),
    path('<int:pk>/', NewDetailView.as_view(), name='new_detail'),
    path('create/', StoryCreate.as_view(), name="story_create"),
]
