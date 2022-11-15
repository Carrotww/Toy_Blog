from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.serializers import ArticleSerializer
from articles.models import Article as ArticleModel
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from articles.paginations import PostPageNumberPagination, PostPageNumberPagination2
from rest_framework.generics import ListAPIView

@permission_classes((permissions.AllowAny,))
class ArticleView(ListAPIView):
    pagination_class = PostPageNumberPagination
    serializer_class = ArticleSerializer
    queryset = ArticleModel.objects.all()
    
    def get(self, request):
        if self.request.GET.get('temp') == 're':
            self.pagination_class = PostPageNumberPagination2
        # queryset = self.filter_queryset(self.get_queryset())
        pages = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(pages, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "글 작성 완료!!"})
        else:
            return Response({"message": f'${serializer.errors}'}, 400)