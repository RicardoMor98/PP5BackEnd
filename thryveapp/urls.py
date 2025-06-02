from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, PostViewSet, CommentViewSet, CategoryViewSet, VoteViewSet
from . import views

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('api/csrf/', views.get_csrf_token),
    path('api/data/', views.get_data),
    path('', include(router.urls)),
]
