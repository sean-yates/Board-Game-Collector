from django.db import models
from django.urls import reverse

# Create your models here.


class Boardgame(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    players = models.CharField(max_length=100)
    playtime = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'boardgame_id': self.id})


class Piece(models.Model):
    name = models.CharField('Piece Name', max_length=100)
    size = models.CharField(max_length=100)

    boardgame = models.ForeignKey(Boardgame, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
