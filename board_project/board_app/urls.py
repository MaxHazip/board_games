from board_app import views
from django.urls import path

urlpatterns = [
    path('', views.root),
    path('game-page', views.page)
]
