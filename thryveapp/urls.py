from django.urls import path, include
from .views import root_view
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, PostViewSet, CommentViewSet, CategoryViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', root_view),  # 👈 Now hitting "/" returns a JSON message
    path('', include(router.urls)),
]
