from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    get_posts,
    CategoryViewSet,
    UserViewSet,
    CommentViewSet,
)

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('categories', CategoryViewSet)
router.register('users', UserViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('posts/get_post/', get_posts, name='get_post'),
]
urlpatterns += router.urls