from django.shortcuts import render
from django.http import HttpResponse

from .models import Board

# Create your views here.
def home(request):
    boards_list = Board.objects.all()
    context = {'boards_list': boards_list}
    return render(request, 'boards/index.html', context)
    # return HttpResponse("this is the home page of BOARDS")