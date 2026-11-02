from rest_framework import serializers
from ..models import Comment, Post, User


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('comment_id',)