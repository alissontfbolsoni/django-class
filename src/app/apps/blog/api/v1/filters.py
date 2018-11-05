import django_filters

from app.apps.blog.models import Post


class PostFilterSet(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = {
            'is_active': ['exact', ],
            'category': ['in', ]
        }
