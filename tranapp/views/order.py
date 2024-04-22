# 订单相关视图
from rest_framework.views import APIView
from rest_framework.response import Response
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import OrderSer
from tranapp import models
from tranapp.utils.auth_ import LoginAuth


class OrderView(MyResponse, APIView):
    """订单视图"""
    authentication_classes = [LoginAuth]

    def get(self, request):
        # print(request.user,request.auth)
        return Response("订单信息")
