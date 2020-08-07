from django.shortcuts import render
from django.http import HttpResponse

from .models import Board

# Create your views here.
def home(request):
    boards_list = Board.objects.all()
    context = {'boards_list': boards_list}
    return render(request, 'boards/index.html', context)
    # return HttpResponse("this is the home page of BOARDS")

def topicsPage(request, pk):
    board = Board.objects.get(id=pk)
    # topics = board.topic_set.all()
    topics = board.topics.all()
    context = {'board': board, 'topics': topics}
    return render(request, 'boards/topics.html', context)