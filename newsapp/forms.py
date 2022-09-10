from django.forms import ModelForm
from .models import News

class CreateStory(ModelForm):
    class Meta:
        model = News
        exclude = ('docname',)
        fields = '__all__'