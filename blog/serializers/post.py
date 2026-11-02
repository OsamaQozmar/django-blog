from rest_framework import serializers
from ..models import Post, User, Category


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        allow_empty=False,
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('title_id',)