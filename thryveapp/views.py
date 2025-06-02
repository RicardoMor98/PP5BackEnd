from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import UserProfile, Post, Category, Comment, Vote
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import (
    UserProfileSerializer, PostSerializer, CategorySerializer,
    CommentSerializer, VoteSerializer
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # 🔎 Filters by query parameters in the URL
    filterset_fields = [
        'author__username',
        'category__name',
        'created_at',
    ]

    # 🔍 Enables keyword-based search
    search_fields = [
        'title',
        'content',
        'author__username',
    ]

    # 🔃 Allows clients to sort results by these fields
    ordering_fields = [
        'created_at',
        'title',
    ]

def perform_create(self, serializer):
    user = self.request.user
    post = serializer.validated_data['post']
    content = serializer.validated_data['content']

    # Check for duplicate comment by the same user on the same post
    if Comment.objects.filter(post=post, author=user, content=content).exists():
        raise serializers.ValidationError("You've already posted this exact comment.")

    serializer.save(author=user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.validated_data['post']
        content = serializer.validated_data['content']

        if Comment.objects.filter(post=post, author=user, content=content).exists():
            raise serializers.ValidationError("You've already posted this exact comment.")

        serializer.save(author=user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = serializer.validated_data['post']
        vote_type = serializer.validated_data['vote_type']
        user = self.request.user
        vote, created = Vote.objects.update_or_create(
            post=post, user=user,
            defaults={'vote_type': vote_type}
        )
        serializer.instance = vote