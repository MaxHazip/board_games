from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BoardGames)
admin.site.register(Genres)
admin.site.register(Profiles)
admin.site.register(BonusCards)
admin.site.register(Orders)
admin.site.register(Cart)
admin.site.register(Purchased)
