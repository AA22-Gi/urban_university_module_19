from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс max_digits
    age = models.PositiveIntegerField()  # Возраст

    def __str__(self):
        return self.name
    #  max_digits=10 общее количество цифр, которые могут быть сохранены в поле,
    #  включая как целую часть, так и дробную.
    #  decimal_places=2 - количество цифр, которое может быть сохранено после десятичной точки
    #  models.PositiveIntegerField() — это тип поля, который используется для хранения целых чисел,
    #  которые должны быть положительными.


class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов
    description = models.TextField()  # Описание
    age_limited = models.BooleanField(default=False)  # Ограничение возраста
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели
    #  models.ManyToManyField(Buyer, related_name='games') — это поле,
    #  которое устанавливает связь "многие ко многим" между моделями.
    def __str__(self):
        return self.title

#  python manage.py makemigrations task1 - создаем миграцию
#  python manage.py migrate -  применяем миграцию
