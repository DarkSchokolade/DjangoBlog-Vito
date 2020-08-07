from django.urls import path
from . import views

app_name = 'boards' #namespacing your app

urlpatterns = [
    path('', views.home, name='home'),
    path('topics/<str:pk>', views.topicsPage, name='topics'),
]