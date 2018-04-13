from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'blog'
urlpatterns = [
    path('recent/', views.PostListView.as_view(), name='recent'),
]
