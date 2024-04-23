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
            print("登录用户信息:",userinfo)
            username = userinfo.get("username")
            password = userinfo.get("password")
            md5_password = md5_.setPassword(password)
            userobj = models.UserInfo.objects.filter(username=username, password=md5_password).first()

            if userobj:
                print("userobj", userobj)

                return userobj, token  # request.user  request.auth
            raise AuthenticationFailed("请先登录")

        except:
          raise AuthenticationFailed("请先登录")
    def authenticate_header(self, request):
        return "API"



class LoginAuth2(BaseAuthentication):
    """登录状态认证（可根据请求判断是否执行）"""
    def __init__(self, user_methods):
        self.user_methods = user_methods


    def authenticate(self, request):
        if request.method == "OPTIONS":
            # 预检不进行权限校验。
            return
        if request.method in self.user_methods:
            # 请求方法与self.user_methods一致的话则不需要执行对应的认证内容。

            return
        try:
            token = request.headers.get("token")
            # 解开token 从获取用户名密码，然后校验
            userinfo = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            username = userinfo.get("username")
            password = userinfo.get("password")
            md5_password = md5_.setPassword(password)
            print(md5_password,username)
            userobj = models.UserInfo.objects.filter(username=username, password=md5_password).first()

            if userobj:
                return userobj, token  # request.user  request.auth
            raise AuthenticationFailed("请先登录")

        except:
          raise AuthenticationFailed("请先登录")
    def authenticate_header(self, request):
        return "API"