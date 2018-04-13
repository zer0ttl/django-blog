from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    pass


class Post(models.Model):
    STATUS_CHOICES = (
        (5, 'Draft'),
        (10, 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default=5)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title