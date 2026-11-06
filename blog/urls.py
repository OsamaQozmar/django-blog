from django.urls import path

from rest_framework.routers import DefaultRouter

from blog.views.generate import generate_post

from .views import (
    PostViewSet,
    get_posts,
    CategoryViewSet,
    UserViewSet,
    CommentViewSet,
    summarize_post_view,
)

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('categories', CategoryViewSet)
router.register('users', UserViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('posts/get_post/', get_posts, name='get_post'),
    path('posts/generate/', generate_post, name='generate_post'),
    path('posts/<int:post_id>/summarize/', summarize_post_view, name='summarize_post'),
]
urlpatterns += router.urls