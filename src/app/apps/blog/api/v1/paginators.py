from rest_framework.pagination import PageNumberPagination


class BlogPaginationAbstract(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'


class CategoryPagination(BlogPaginationAbstract):
    pass


class PostPagination(BlogPaginationAbstract):
    pass
