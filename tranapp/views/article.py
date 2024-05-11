# 帖子相关
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from tranapp.utils.filt_ import BookByTypeFilter
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import ArticlSer, ArticlCommentSer, ArticlCommentSer2
from tranapp.utils.auth_ import LoginAuth
from tranapp.utils.filt_ import AddressByUserFilter
from tranapp import models


class ArticleView(MyResponse, ModelViewSet):
    """帖子视图"""
    authentication_classes = [LoginAuth]
    pagination_class = LimitOffsetPagination
    queryset = models.Article.objects.all().order_by("-create_time")
    serializer_class = ArticlSer

    def perform_create(self, serializer):
        userinfo = self.request.user
        serializer.save(author=userinfo)


class SelfAtricleView(MyResponse, APIView):
    def get(self, request):
        return Response("获取自己发布的帖子")

# 下面这些视图的封装性较低，适合初学者看

class CommentView(MyResponse, APIView):
    """帖子评论"""
    authentication_classes = [LoginAuth]

    def get(self, request):
        article_id = int(request.query_params.get("article_id"))
        queryset = models.ArticleComment.objects.filter(article_id=article_id).all()
        ser = ArticlCommentSer(instance=queryset, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = ArticlCommentSer2(data=request.data)
        ser.is_valid(raise_exception=True)
        print(ser.validated_data)
        instance = models.ArticleComment.objects.create(**ser.validated_data)
        ser2 = ArticlCommentSer(instance=instance)
        return Response(ser2.data)

    def delete(self, request,pk):
        userinfo = request.user

        return Response("删除成功")
# class CommentDetailView(MyResponse, APIView):
#     """评论详情"""
#     authentication_classes = [LoginAuth]
#     def delete(self,request,pk):
#         user = request.user
#         author_id = models.ArticleComment.objects.filter(id=pk).get("id")

