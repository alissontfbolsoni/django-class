from rest_framework import serializers

from app.apps.blog.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'is_active', 'created_at')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'is_active', 'created_at')
