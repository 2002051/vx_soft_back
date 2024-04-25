# 一些其它视图
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from tranapp.utils.auth_ import LoginAuth
from tranapp.utils.filt_ import CartByUserFilter
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import BannerSer
from tranapp import models


class BannerView(MyResponse, APIView):
    """轮播图获取"""

    def get(self, request):
        print("xxx")
        queryset = models.Banner.objects.all()
        ser = BannerSer(instance=queryset, many=True)
        return Response(ser.data)
