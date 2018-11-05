from rest_framework import routers

from .views import CategoryViewSet, PostViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)
