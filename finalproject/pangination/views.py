from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.


def post_list(request):
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 5)  # 5 постов на странице

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'pangination/post_list.html', {'posts': posts, 'paginator': paginator})


def post_list_2(request):
    post_list = Post.objects.all().order_by('created_at')

    items_per_page = request.GET.get('items_per_page', 3)  # По умолчанию 5 постов на странице
    paginator = Paginator(post_list, items_per_page)  # Используем выбранное количество постов

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'pangination/post_list_2.html', {
        'posts': posts,
        'paginator': paginator,
        'items_per_page': items_per_page
    })