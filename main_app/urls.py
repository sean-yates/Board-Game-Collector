from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boardgames/', views.boardgames_index, name='index'),
    path('boardgames/<int:boardgame_id>',
         views.boardgames_detail, name='detail'),
    path('boardgames/create/', views.BoardgameCreate.as_view(),
         name='boardgames_create'),
    path('boardgames/<int:pk>/update/',
         views.BoardgameUpdate.as_view(), name='boardgames_update'),
    path('boardgames/<int:pk>/delete/',
         views.BoardgameDelete.as_view(), name='boardgames_delete'),
    path('boardgames/<int:boardgame_id>/add_piece/',
         views.add_piece, name='add_piece'),
    path('boardgamess/<int:boardgame_id>/assoc_gamestore/<int:gamestore_id>/',
         views.assoc_gamestore, name='assoc_gamestore'),


    # gamestore urls
    path('gamestores/', views.gamestore_index, name='all_gamestores'),
    path('gamestores/<int:gamestore_id>/',
         views.gamestore_detail, name='gamestore_detail'),
    path('gamestore/create/', views.Create_Gamestore.as_view(),
         name='create_gamestore'),
    path('gamestores/<int:pk>/update/',
         views.Update_gamestore.as_view(), name='update_gamestore'),
    path('gamestores/<int:pk>/delete/',
         views.Delete_gamestore.as_view(), name='delete_gamestore'),
]
