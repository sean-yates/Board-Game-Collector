from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from django.http import HttpResponse


# Our Models
from .models import Boardgame
from .forms import PieceForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def boardgames_index(request):
    boardgames = Boardgame.objects.all()
    return render(request, 'boardgames/index.html', {'boardgames': boardgames})


def boardgames_detail(request, boardgame_id):
    boardgame = Boardgame.objects.get(id=boardgame_id)
    piece_form = PieceForm()
    context = {
        'boardgame': boardgame,
        'piece_form': piece_form
    }
    return render(request, 'boardgames/detail.html', context)


class BoardgameCreate(CreateView):
    model = Boardgame
    fields = '__all__'


class BoardgameUpdate(UpdateView):
    model = Boardgame
    # Let's disallow the renaming of a Boardgame by excluding the name field!
    fields = ['genre', 'players', 'playtime']


class BoardgameDelete(DeleteView):
    model = Boardgame
    success_url = '/boardgames/'


def add_piece(request, boardgame_id):
    form = PieceForm(request.POST)
    if form.is_valid():
        new_piece = form.save(commit=False)
        new_piece.boardgame_id = boardgame_id
        new_piece.save()
    return redirect('detail', boardgame_id=boardgame_id)
