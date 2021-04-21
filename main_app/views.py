from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from django.http import HttpResponse


# Our Models
from .models import Boardgame, Gamestore
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
    gamestores_boardgame_doesnt_have = Gamestore.objects.exclude(
        id__in=boardgame.gamestores.all().values_list('id'))
    piece_form = PieceForm()
    context = {
        'boardgame': boardgame,
        'piece_form': piece_form,
        'gamestores': gamestores_boardgame_doesnt_have
    }
    return render(request, 'boardgames/detail.html', context)


class BoardgameCreate(CreateView):
    model = Boardgame
    fields = ['name', 'genre', 'players', 'playtime']


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

# Gamestore views


def gamestore_index(request):
    gamestores = Gamestore.objects.all()
    context = {'gamestores': gamestores}

    return render(request, 'gamestore/index.html', context)


def gamestore_detail(request, gamestore_id):
    gamestore = Gamestore.objects.get(id=gamestore_id)
    context = {
        'gamestore': gamestore
    }
    return render(request, 'gamestore/detail.html', context)


class Create_Gamestore(CreateView):
    model = Gamestore
    fields = '__all__'


class Update_gamestore(UpdateView):
    model = Gamestore
    fields = ['location']


class Delete_gamestore(DeleteView):
    model = Gamestore
    success_url = '/gamestores/'


def assoc_gamestore(request, boardgame_id, gamestore_id):
    # Note that you can pass a toy's id instead of the whole object
    Boardgame.objects.get(id=boardgame_id).gamestores.add(gamestore_id)
    return redirect('detail', boardgame_id=boardgame_id)
