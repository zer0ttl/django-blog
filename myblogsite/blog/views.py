from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/recent.html'

    # We need to show only the published posts. Drafts posts will not be shown.
    def get_queryset(self):
        return Post.objects.filter(status=10)