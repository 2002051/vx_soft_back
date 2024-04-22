# 地址相关
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from tranapp.utils.filt_ import BookByTypeFilter
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import BookSer, TypeSer
from tranapp import models



class AddressView(MyResponse,APIView):
    def get(self,request):
        return Response("ok")
