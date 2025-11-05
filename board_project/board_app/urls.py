from board_app import views
from django.urls import path

urlpatterns = [
    path('', views.root),
    path('game-pages/<int:item_id>', views.page)
]
