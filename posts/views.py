from typing import List
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
from comments.forms import FormComment
from comments.models import Comment
from django.contrib import messages
from django.db import connection

class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 10
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('category')
        qs = qs.order_by('-id').filter(publish=True)
        qs = qs.annotate(
            number_comments=Count(
                Case(
                    When(comment__publish=True, then=1)
                )
            )
        )

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['connection'] = connection
        return context


class PostSearch(PostIndex):
    template_name = 'posts/post_search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        term = self.request.GET.get('term')

        if not term:
            return qs

        qs = qs.filter(
            Q(name__icontains=term) |
            Q(author__first_name__iexact=term) |
            Q(description__icontains=term) |
            Q(resume__icontains=term) |
            Q(category__name__iexact=term)
        )        

        return qs


class PostCategory(PostIndex):
    template_name = 'posts/post_category.html'

    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)
        if not category:
            return qs

        qs = qs.filter(category__name__iexact=category)

        return qs


class PostShow(View):
    template_name = 'posts/show.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, publish=True)
        self.context = {
            'post': post,
            'comments': Comment.objects.filter(post_comment=post, publish=True),
            'form': FormComment(request.POST or None),
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.context['form']

        if not form.is_valid():
            return render(request, self.template_name, self.context)

        comment = form.save(commit=False)

        if request.user.is_authenticated:
            comment.user_comment = request.user

        comment.post_comment = self.context['post']
        comment.save()
        messages.success(request, 'Seu comentário foi enviado para revisão.')
        return redirect('post_show', pk=self.kwargs.get('pk'))

"""
class PostShow(UpdateView):
    template_name = 'posts/show.html'
    model = Post
    form_class = FormComment
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        comments = Comment.objects.filter(
            publish=True,
            post_comment=post.id
        )

        context['comments'] = comments

        return context

    def form_valid(self, form):
        post = self.get_object()
        comment = Comment(**form.cleaned_data)
        comment.post_comment = post

        if self.request.user.is_authenticated:
            comment.user_comment = self.request.user
        
        comment.save()
        messages.success(self.request, 'Comentário enviado com sucesso!')
        return redirect('post_show', pk=post.id)
"""


