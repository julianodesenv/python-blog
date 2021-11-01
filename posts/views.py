from typing import List
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
from comments.forms import FormComment
from comments.models import Comment
from django.contrib import messages


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 2
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publish=True)
        qs = qs.annotate(
            number_comments=Count(
                Case(
                    When(comment__publish=True, then=1)
                )
            )
        )

        return qs


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

