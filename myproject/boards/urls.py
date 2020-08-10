from django.urls import path
from . import views

app_name = 'boards' #namespacing your app

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('', views.home, name='home'),
    path('topics/<str:pk>', views.topicsPage, name='topics'),
]