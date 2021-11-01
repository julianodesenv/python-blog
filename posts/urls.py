from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:category>', views.PostCategory.as_view(), name='post_category'),
    path('busca', views.PostSearch.as_view(), name='post_search'),
    path('post/<int:pk>', views.PostShow.as_view(), name='post_show'),
]