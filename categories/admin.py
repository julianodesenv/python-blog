from django.contrib import admin
from .models import Categories


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Categories, CategoriesAdmin)