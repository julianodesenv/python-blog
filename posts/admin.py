from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'author', 'date', 'category', 'publish',)
    list_editable = ('publish',)
    list_display_links = ('id', 'name',)
    summernote_fields = ('description',)


admin.site.register(Post, PostAdmin)