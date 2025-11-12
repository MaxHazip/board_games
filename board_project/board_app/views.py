from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def root(request):

    board_games = BoardGames.objects.all()
    genres = Genres.objects.all()
    query = request.GET.get('search', '')
    results = []

    if query:
        results = BoardGames.objects.filter(
            name__icontains=query
        )

    genres_req = request.GET.get('genres', '')

    if genres_req:
        board_games = BoardGames.objects.filter(games_genres=genres_req)

    
    context = {
        "board_games": board_games,
        "genres": genres,
        "query": query,
        "results": results,
    }
    return render(request, 'main-content.html', context)

def page(request, item_id: int):
    game = BoardGames.objects.filter(id=item_id)
    game = get_object_or_404(game)

    context = {
        'game': game,
    }
    return render(request, 'game-page.html', context)