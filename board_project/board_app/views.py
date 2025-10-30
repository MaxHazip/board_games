from django.shortcuts import render
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