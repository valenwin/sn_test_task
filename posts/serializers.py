from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField('get_likes')
    dislikes_count = serializers.SerializerMethodField('get_dislikes')

    class Meta:
        model = Post
        fields = ('id', 'owner', 'body', 'created', 'likes_count', 'dislikes_count')

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    @staticmethod
    def get_likes(post):
        return post.like_voters.count()

    @staticmethod
    def get_dislikes(post):
        return post.dislike_voters.count()
