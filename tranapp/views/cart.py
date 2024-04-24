# 购物车相关视图
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from tranapp.utils.auth_ import LoginAuth
from tranapp.utils.filt_ import CartByUserFilter
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import CartSer
from tranapp import models


class CartView(MyResponse, ModelViewSet):
    """购物车条目"""
    authentication_classes = [LoginAuth]
    serializer_class = CartSer
    queryset = models.Cart.objects.all()
    filter_backends = [CartByUserFilter]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        userinfo = self.request.user
        serializer.save(user=userinfo)
