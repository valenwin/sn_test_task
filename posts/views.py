from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = IsAuthenticated, IsOwnerOrReadOnly
        else:
            self.permission_classes = IsAuthenticated,
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})

    def perform_update(self, serializer):
        serializer.save(**{'owner': self.request.user})

    @action(detail=True)
    def like(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        post.like_voters.add(request.user)
        post.dislike_voters.remove(request.user)
        post.save()
        return Response({'response': f'You like {post.id} post.'}, status=status.HTTP_200_OK)

    @action(detail=True)
    def dislike(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        post.dislike_voters.add(request.user)
        post.like_voters.remove(request.user)
        post.save()
        return Response({'response': f'You dislike {post.id} post.'}, status=status.HTTP_200_OK)
