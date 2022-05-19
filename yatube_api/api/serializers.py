from django.contrib.auth import get_user_model
from rest_framework import serializers
from posts.models import Comment, Group, Post


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(many=False,
                                              read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text',
                  'created')
