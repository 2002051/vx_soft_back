# 地址相关
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from tranapp.utils.filt_ import BookByTypeFilter
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import AddressSer
from tranapp.utils.auth_ import LoginAuth
from tranapp.utils.filt_ import AddressByUserFilter
from tranapp import models


class AddressView(MyResponse, ModelViewSet):
    """地址视图"""
    authentication_classes = [LoginAuth]
    queryset = models.Address.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = AddressSer
    filter_backends = [AddressByUserFilter]
    def perform_create(self, serializer):
        userinfo = self.request.user
        serializer.save(userinfo=userinfo)
