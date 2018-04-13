from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.


class TagInline(admin.TabularInline):
    model = models.Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag_list', 'author', 'publish', 'status')
    list_filter = ('status', 'created_at', 'publish', 'author', 'tags')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Post, PostAdmin)