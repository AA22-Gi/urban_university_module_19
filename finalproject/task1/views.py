from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer


# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')


def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']

    context = {
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')


users = Buyer.objects.all()
usernames_list = list(Buyer.objects.values_list('name', flat=True))


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in usernames_list:
                info['error'] = 'Пользователь уже существует'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info['message'] = f'Приветствуем, {username}!'
        else:
            form = UserRegister()
            info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)
