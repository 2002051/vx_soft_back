# 用户相关视图
from rest_framework.views import APIView
from rest_framework.response import Response
from tranapp.utils.res_ import MyResponse
from tranapp.utils.auth_ import LoginAuth
from tranapp.utils.ser_ import RegisterSer, LoginSer, CampusSer, EditUserSer
from tranapp import models


class RegisterView(MyResponse, APIView):
    """注册"""

    def post(self, request):
        ser = RegisterSer(data=request.data)
        ser.is_valid(raise_exception=True)  # 校验逻辑在序列化器的钩子方法
        ser.save()
        return Response(ser.data)


class EditView(MyResponse, APIView):
    authentication_classes = [LoginAuth]
    """编辑用户信息"""

    def put(self, request):
        userinfo = request.user
        instance = models.UserInfo.objects.filter(id=userinfo.id).first()
        ser = EditUserSer(data=request.data, instance=instance)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class LoginView(MyResponse, APIView):
    """登录视图"""
    def post(self, request):
        ser = LoginSer(data=request.data)
        ser.is_valid(raise_exception=True)  # 序列化器钩子包含用户名密码校验以及生成jwt
        token = ser.validated_data.pop("token")
        instance = models.UserInfo.objects.filter(**ser.data).first()
        ser2 = LoginSer(instance=instance)
        return Response({"user": ser2.data, "token": token})





class CampusView(MyResponse, APIView):
    def get(self, request):
        queryset = models.Campus.objects.all()
        ser = CampusSer(instance=queryset, many=True)
        return Response(ser.data)
