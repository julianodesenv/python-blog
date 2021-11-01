from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'post_comment', 'date', 'publish',)
    list_editable = ('publish',)
    list_display_links = ('id', 'name', 'email',)


admin.site.register(Comment, CommentAdmin)