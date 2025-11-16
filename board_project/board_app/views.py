from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def root(request):

    board_games = BoardGames.objects.all().order_by('-add_date')
    genres = Genres.objects.all()
    query = request.GET.get('search', '')
    genres_req = request.GET.get('genres', '')
    sort = request.GET.get('sort', '')


    if query or genres_req:
        board_games = (
            BoardGames
            .objects
            .filter(
                games_genres=genres_req,
                name__icontains=query
            ).order_by('-add_date')
        )

    if sort == 'date-reverse':
        board_games.order_by('add_date')
    
    context = {
        "board_games": board_games,
        "genres": genres,
        "query": query,
    }
    return render(request, 'main-content.html', context)

def page(request, item_id: int):
    game = BoardGames.objects.filter(id=item_id)
    game = get_object_or_404(game)

    game.popularity += 1
    game.save()

    

    context = {
        'game': game,
    }
    return render(request, 'game-page.html', context)