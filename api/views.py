
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, mixins
from .models import Post, Group, Follow
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
                          PostSerializer,
                          CommentSerializer,
                          GroupSerializer,
                          FollowSerializer
                          )

from .permissions import IsOwnerOrReadOnly
from .filter import IsOwnerFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin,
                   mixins.ListModelMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]


class FollowViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin,
                    mixins.ListModelMixin):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Follow.objects.all()
    filter_backends = [filters.SearchFilter, IsOwnerFilterBackend]
    filterset_fields = ['following']
    search_fields = ['=user__username', '=following__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
