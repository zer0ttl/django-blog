from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('recent/', views.PostListView.as_view(), name='recent'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
