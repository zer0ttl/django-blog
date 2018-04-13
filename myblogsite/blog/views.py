from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/recent.html'

    # We need to show only the published posts. Drafts posts will not be shown.
    def get_queryset(self):
        return Post.objects.filter(status=10)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
