from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
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
        # print(self.request.GET.get('temp'))
        self.pagination_class = PostPageNumberPagination2
        queryset = self.filter_queryset(self.get_queryset())
        pages = self.paginate_queryset(queryset)

        serializer = self.get_serializer(pages, many=True)

        return self.get_paginated_response(serializer.data)
    # def get_queryset(self):
        
    #     print(self.request.GET.get('temp',''))
    #     return
    
    # def filter_queryset(self, queryset):
    #     filter_backends = [CategoryFilter]

    #     if 'geo_route' in self.request.query_params:
    #         filter_backends = [GeoRouteFilter, CategoryFilter]
    #     elif 'geo_point' in self.request.query_params:
    #         filter_backends = [GeoPointFilter, CategoryFilter]

    #     for backend in list(filter_backends):
    #         queryset = backend().filter_queryset(self.request, queryset, view=self)

    #     return queryset

    
    # def list(self, request):
    #     # temp = request.GET.get('temp', '')
    #     # if temp == 'temp':
    #         # return ArticleModel.objects.all().order_by('title')
    #     queryset = self.get_queryset()
    #     slz = ArticleSerializer(queryset, many=True)
    #     return Response(slz.data)
    #     # articles = ArticleModel.objects.all()
    #     # serializer = ArticleSerializer(articles, many=True).data
    #     # return Response(serializer, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "글 작성 완료!!"})
        else:
            return Response({"message": f'${serializer.errors}'}, 400)