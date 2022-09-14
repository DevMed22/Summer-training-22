from django.urls import path
from .views import HomePageView , PathoView
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('path/',PathoView.as_view(),name='patho'),
]