from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, PostViewSet, CommentViewSet, CategoryViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]