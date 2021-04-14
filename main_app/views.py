from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse
from .boardgameclass import boardgames
# Define the home view


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def boardgames_index(request):
    return render(request, 'boardgames/index.html', {'boardgames': boardgames})
