from django.contrib import admin

from .models.category import Category
from .models.post import Post
from .models.comment import Comment
from .models.user import User


#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')
    ordering = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'post', 'created_at')
    list_filter = ('author', 'post', 'created_at','content')
    search_fields = ('content','post')
    ordering = ('content',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    list_filter = ('username' ,'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)