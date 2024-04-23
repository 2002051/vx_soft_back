# 图书相关视图
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from tranapp.utils.auth_ import LoginAuth2,LoginAuth
from tranapp.utils.filt_ import BookByTypeFilter, BookByCampus
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import BookSer, TypeSer
from tranapp import models


def Selsct_auth(cls, user_method):
    def inner():
        obj = cls(user_method)
        return obj

    return inner


class TypeView(MyResponse, APIView):
    """书籍类别表"""

    def get(self, request):
        queryset = models.Type.objects.all()
        ser = TypeSer(instance=queryset, many=True)
        return Response(ser.data)


class BookView(MyResponse, ModelViewSet):
    """常规图书视图,获取全部需要分页"""
    # authentication_classes = [Selsct_auth(LoginAuth2, ["GET"])]
    authentication_classes = [LoginAuth]
    serializer_class = BookSer
    queryset = models.Book.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [BookByTypeFilter, BookByCampus]  # 如果请求参数中query携带了type 那么就会根据type进行过滤，否则啥也不做

    def perform_create(self, serializer):
        userinfo = self.request.user
        print("userinfo", userinfo)
        serializer.save(userinfo=userinfo)


class BookTView(MyResponse, APIView):
    """根据类别获取图书列表"""

    def get(self, request, tid):
        return Response("ok")
