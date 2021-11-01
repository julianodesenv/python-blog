from django.db import models
from categories.models import Categories
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name='Título')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    resume = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, blank=True, null=True)
    image = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True)
    publish = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name