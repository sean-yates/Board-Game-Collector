from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boardgames/', views.boardgames_index, name='index'),
    path('boardgames/<int:boardgame_id>',
         views.boardgames_detail, name='detail')

]
