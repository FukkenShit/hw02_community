"""
Админка приложения posts.
"""

from django.contrib import admin
from .models import Post, Group


class GroupAdmin(admin.ModelAdmin):
    """Админка модели Group."""
    list_display = (
        'title',
        'slug',
        'description'
    )


class PostAdmin(admin.ModelAdmin):
    """Админка модели Post."""
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = ('group',)
    empty_value_display = '-пусто-'


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
