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
]
