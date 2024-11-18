from django.contrib import admin
from .models import Buyer, Game


# Регистрация модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Отображение полей в списке
    search_fields = ('name',)  # Поля для поиска
    list_filter = ('age',)  # Фильтрация по возрасту

# Регистрация модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')  # Отображение полей в списке
    search_fields = ('title',)  # Поля для поиска
    list_filter = ('age_limited',)  # Фильтрация по ограничению возраста