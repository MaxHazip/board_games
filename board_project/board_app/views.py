from django.shortcuts import render
from .models import *

# Create your views here.
def root(request):

    board_game = BoardGames.objects.first()
    
    context = {
        "board_game": board_game,
    }
    return render(request, 'main-content.html', context)