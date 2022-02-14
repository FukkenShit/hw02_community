from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post, Group

PER_PAGE = 10


def index(request):
    """Главная страница со списком постов."""
    template = 'posts/index.html'
    posts = Post.objects.all()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Страниа со списком постов группы."""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'page_obj': page_obj
    }
    return render(request, template, context)
