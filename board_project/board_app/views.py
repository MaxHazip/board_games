from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def root(request):

    board_games = BoardGames.objects.all()
    genres = Genres.objects.all()
    query = request.GET.get('search', '')
    genres_req = request.GET.get('genres', '')
    sort = request.GET.get('sort', '')


    if query:
        board_games = BoardGames.objects.filter(name__icontains=query)

    if genres_req:
        board_games = BoardGames.objects.filter(games_genres__name=genres_req)

    match sort:
        case "date-reverse":
            board_games = board_games.order_by("add_date")
        case "price-asc":
            board_games = board_games.order_by("price")
        case "price-des":
            board_games = board_games.order_by("-price")
        case "alphabet":
            board_games = board_games.order_by("name")
        case "reverse-alphabet":
            board_games = board_games.order_by("-name")
        case "popular":
            board_games = board_games.order_by("-popularity")
        case "reverse-popular":
            board_games = board_games.order_by("popularity")
        case _:
            board_games = board_games.order_by("-add_date")

    
    context = {
        "board_games": board_games,
        "genres": genres,
        "query": query,
        "sort": sort,
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