from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.
from django.http import HttpResponse


# Our Models
from .models import Boardgame


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def boardgames_index(request):
    boardgames = Boardgame.objects.all()
    return render(request, 'boardgames/index.html', {'boardgames': boardgames})


def boardgames_detail(request, boardgame_id):
    boardgame = Boardgame.objects.get(id=boardgame_id)
    context = {
        'boardgame': boardgame
    }
    return render(request, 'boardgames/detail.html', context)


class BoardgameCreate(CreateView):
    model = Boardgame
    fields = '__all__'
