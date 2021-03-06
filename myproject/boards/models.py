from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics') #  But if we don’t set a name for it, Django will generate it with the name: (class_name)_set
    starter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='topics')

    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic =models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')   # This instructs Django that we don’t need this reverse relationship, so it will ignore it.

    def __str__(self):
        return self.message