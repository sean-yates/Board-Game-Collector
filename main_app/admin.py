from django.contrib import admin

from .models import Boardgame, Piece
# Register your models here.
admin.site.register(Boardgame)
admin.site.register(Piece)
