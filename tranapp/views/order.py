# 订单相关视图
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from tranapp.utils.filt_ import OrderByUserFilter, OrderBySellerFilter
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import OrderSer
from tranapp import models
from tranapp.utils.auth_ import LoginAuth


class OrderView(MyResponse, ModelViewSet):
    """用户视角订单视图"""
    authentication_classes = [LoginAuth]
    # pagination_class = LimitOffsetPagination
    pagination_class = None  # 禁用全局分页组件

    serializer_class = OrderSer
    queryset = models.Order.objects.all()
    filter_backends = [OrderByUserFilter]

    def perform_create(self, serializer):
        userinfo = self.request.user

        status = int(serializer.validated_data['status'])
        if status == 1:
            """表示是直接购买的"""
            book = models.Book.objects.filter(id=int(serializer.validated_data["book_id"])).first()
            book.active = 2
            book.save()
        serializer.save(user=userinfo)

    def perform_update(self, serializer):
        print("ser", serializer.validated_data)
        userinfo = self.request.user
        cart_item = models.Cart.objects.filter(user=userinfo, book_id=int(serializer.validated_data["book_id"])).first()
        print("cart_item", cart_item.id)
        models.Cart.objects.filter(id=cart_item.id).delete()
        book = models.Book.objects.filter(id=int(serializer.validated_data["book_id"])).first()
        book.active = 2
        book.save()
        serializer.save()


class OrderSellView(MyResponse, ModelViewSet):
    """卖家视角订单视图"""
    authentication_classes = [LoginAuth]
    # pagination_class = LimitOffsetPagination
    pagination_class = None  # 禁用全局分页组件
    serializer_class = OrderSer
    queryset = models.Order.objects.all()
    filter_backends = [OrderBySellerFilter]
