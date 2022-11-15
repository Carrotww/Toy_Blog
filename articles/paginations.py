from rest_framework.pagination import CursorPagination

class PostPageNumberPagination(CursorPagination):
    page_size = 4
    ordering = '-created_at'
    
    # cursor_query_param = 'page'
    # max_page_size = 50
    # page_query_param = 'p'

class PostPageNumberPagination2(CursorPagination):
    page_size = 4
    ordering = 'created_at'