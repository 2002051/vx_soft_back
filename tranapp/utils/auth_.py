# 认证，部分请求没有登录是无法发送成功的..
from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from tranapp.utils import md5_
from tranapp import models
from rest_framework.exceptions import AuthenticationFailed

class LoginAuth(BaseAuthentication):
    """登录状态认证"""

    def authenticate(self, request):
        if request.method == "OPTIONS":
            # 预检不进行权限校验。
            return
        try:
            token = request.headers.get("token")
            # 解开token 从获取用户名密码，然后校验
            userinfo = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            username = userinfo.get("username")
            password = userinfo.get("password")
            md5_password = md5_.setPassword(password)
            userobj = models.UserInfo.objects.filter(username=username, password=md5_password).first()
            if userobj:
                return userobj, token  # request.user  request.auth
        except:
          raise AuthenticationFailed("请先登录")
    def authenticate_header(self, request):
        return "API"
