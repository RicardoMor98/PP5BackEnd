from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, PostViewSet, CommentViewSet, CategoryViewSet, VoteViewSet
from django.urls import path
from . import views
from django.urls import path
from .views import get_csrf_token

urlpatterns = [
    path('api/csrf/', get_csrf_token),
]

urlpatterns = [
    path('api/data/', views.get_data),
]

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
