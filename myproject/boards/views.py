from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import TopicForm, UserCreationForm

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account Created as: ' + user)
            return redirect('boards:login')
    context = {'form': form}
    return render(request, 'boards/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('boards:home')
        else:
            messages.info(request, 'Password or Username is incorect')
    return render(request, 'boards/login.html')

def logoutUser(request):
    logout(request)
    return redirect('boards:login')

@login_required(login_url='boards:login')
def home(request):
    boards_list = Board.objects.all()
    context = {'boards_list': boards_list}
    return render(request, 'boards/index.html', context)
    # return HttpResponse("this is the home page of BOARDS")

@login_required(login_url='boards:login')
def topicsPage(request, pk):
    board = Board.objects.get(id=pk)
    # form = TopicForm(initial={'board': board, 'starter': request.user})
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
        else:
            print(form._errors)

    # topics = board.topic_set.all()
    topics = board.topics.all()
    context = {'board': board, 'topics': topics, 'form': form}
    return render(request, 'boards/topics.html', context)