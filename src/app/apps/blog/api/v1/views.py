from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from app.apps.blog.models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from .paginators import CategoryPagination, PostPagination
from .filters import PostFilterSet


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('is_active', )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = (DjangoFilterBackend, )
    filter_class = PostFilterSet
