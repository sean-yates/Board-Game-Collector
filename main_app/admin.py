from django.contrib import admin

from .models import Boardgame, Piece, Gamestore
# Register your models here.
admin.site.register(Boardgame)
admin.site.register(Piece)
admin.site.register(Gamestore)

