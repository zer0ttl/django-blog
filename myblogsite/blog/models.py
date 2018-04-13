from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    alias = models.CharField(max_length=100)
    pass



class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    STATUS_CHOICES = (
        (5, 'Draft'),
        (10, 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='posts',
                               on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=5)
    summary = models.TextField(default='')
    tags = models.ManyToManyField(Tag, related_name="tagged_posts")

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def tag_list(self):
        return ', '.join([tag['tag_name'] for tag in self.tags.values()])
