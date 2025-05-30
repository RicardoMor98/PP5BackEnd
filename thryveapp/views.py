from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import UserProfile, Post, Category, Comment, Vote
from .serializers import (
    UserProfileSerializer, PostSerializer, CategorySerializer,
    CommentSerializer, VoteSerializer
)
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]