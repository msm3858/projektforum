from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'board': board})
