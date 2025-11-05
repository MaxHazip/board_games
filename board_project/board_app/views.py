from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def root(request):

    board_games = BoardGames.objects.all()
    genres = Genres.objects.all()
    
    context = {
        "board_games": board_games,
        "genres": genres,
    }
    return render(request, 'main-content.html', context)

def page(request, item_id: int):
    game = BoardGames.objects.filter(id=item_id)
    game = get_object_or_404(game)

    context = {
        'game': game,
    }
    return render(request, 'game-page.html', context)