# 用户相关视图
from rest_framework.views import APIView
from rest_framework.response import Response
from tranapp.utils.res_ import MyResponse
from tranapp.utils.ser_ import RegisterSer, LoginSer
from tranapp import models


class RegisterView(MyResponse, APIView):
    """注册"""

    def post(self, request):
        ser = RegisterSer(data=request.data)
        ser.is_valid(raise_exception=True)  # 校验逻辑在序列化器的钩子方法
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
