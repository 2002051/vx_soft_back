# 订单相关视图
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from tranapp.utils.filt_ import OrderByUserFilter
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import OrderSer
from tranapp import models
from tranapp.utils.auth_ import LoginAuth


class OrderView(MyResponse, ModelViewSet):
    """订单视图"""
    authentication_classes = [LoginAuth]
    pagination_class = LimitOffsetPagination
    serializer_class = OrderSer
    queryset = models.Order.objects.all()
    filter_backends = [OrderByUserFilter]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        userinfo = self.request.user
        serializer.save(user=userinfo)
