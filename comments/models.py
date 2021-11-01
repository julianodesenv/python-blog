from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    comment = models.TextField(verbose_name='Comentário')
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name