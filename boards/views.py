from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, User, Topic, Post
from .forms import NewTopicForm
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
        # TODO: redirect to the created topic
            return redirect('boards:board_topics', pk=board.pk)
    else:
        form = NewTopicForm()

    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})
