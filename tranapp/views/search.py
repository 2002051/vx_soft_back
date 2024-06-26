# 查询相关视图
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from tranapp.utils.auth_ import LoginAuth
from tranapp.utils.filt_ import CartByUserFilter
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import BookSer
from tranapp import models


class BookSearchVie(MyResponse, APIView):
    """查询书籍"""
    authentication_classes = [LoginAuth]

    def get(self, request):
        wd = request.query_params.get("wd")
        user = request.user
        from django.db.models import Q
        not_equal_condition = ~Q(userinfo__id=user.id)

        if wd:
            queryset = models.Book.objects.filter(not_equal_condition,userinfo__campus_id=user.campus.id, name__icontains=wd).filter(active=1)
        else:
            queryset = models.Book.objects.filter(userinfo__campus_id=user.campus.id).filter(active=1)
        ser = BookSer(instance=queryset, many=True)
        return Response(ser.data)
