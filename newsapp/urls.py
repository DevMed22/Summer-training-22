from django.urls import path
from .views import NewPageView, NewDetailView


urlpatterns = [
    path('', NewPageView.as_view(), name='news'),
    path('<int:pk>/', NewDetailView.as_view(), name='new_detail')
]
