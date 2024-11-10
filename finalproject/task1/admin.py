from django.contrib import admin
from .models import Buyer, Game
# Register your models here.

admin.site.register([Buyer, Game])
