from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Topic

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['subject']
        # fields = '__all__'
        # exclude = ['starter']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']