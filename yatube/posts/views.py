from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    """Главная страница со списком постов."""
    template = 'posts/index.html'
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Страниа со списком постов группы."""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
