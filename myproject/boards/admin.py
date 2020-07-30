from django.contrib import admin
from .models import *
# Register your models here.

# class TopicInline(admin.TabularInline):
#     model = Topic

class BoardAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    # inlines = [TopicInline]

admin.site.register(Board, BoardAdmin)
admin.site.register(Topic)
admin.site.register(Post)