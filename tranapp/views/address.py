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

    ## 如果创建的地址，或者修改的地址里面is_default 为true 那么就把其它的都改为false
    def perform_create(self, serializer):
        is_default = serializer.validated_data.get("is_default")
        if is_default:
            queryset = models.Address.objects.filter(userinfo_id=self.request.user.id).all()
            for query in queryset:
                query.is_default = False
                query.save()
        userinfo = self.request.user
        serializer.save(userinfo=userinfo)

    def perform_update(self, serializer):
        is_default = serializer.validated_data.get("is_default")
        if is_default:
            queryset = models.Address.objects.filter(userinfo_id=self.request.user.id).all()
            for query in queryset:
                query.is_default = False
                query.save()
        serializer.save()

    ## 如果删掉的是默认地址，那么就选取第一个地址作为默认地址
    def perform_destroy(self, instance):
        is_default = instance.is_default
        userinfo = self.request.user
        instance.delete()
        if is_default:
            obj = models.Address.objects.filter(userinfo_id=userinfo.id).first()
            obj.is_default = True
            obj.save()


class AddDefault(MyResponse, APIView):
    """小程序端点击某地址设置为默认地址"""
    authentication_classes = [LoginAuth]

    def put(self, request, pk):
        userinfo = request.user
        queryset = models.Address.objects.filter(userinfo_id=userinfo.id).all()
        obj = models.Address.objects.filter(id=pk, userinfo_id=userinfo.id).first()

        if obj:
            for query in queryset:
                query.is_default = False
                query.save()
            obj.is_default = True
            obj.save()
            return Response("ok")
        return Response("no_found")
