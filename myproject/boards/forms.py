from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Topic

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        # exclude = ['starter']