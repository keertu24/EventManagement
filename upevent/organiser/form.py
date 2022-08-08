from dataclasses import field
from django.forms import ModelForm
from organiser.models import News

class NewsForm(ModelForm):
    class Meta:
        model=News
        fields=['news_title','image','desc']