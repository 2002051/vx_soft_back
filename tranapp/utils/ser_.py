# 序列化器
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from tranapp import models
from tranapp.utils import md5_
from tools.jwt_ import get_jwt
import datetime


########################### 用户相关 ########################################

class RegisterSer(serializers.ModelSerializer):
    """登录序列化器"""

    class Meta:
        model = models.UserInfo
        fields = "__all__"

    def validate(self, attrs):
        # 执行校验逻辑
        username = attrs.get("username")
        password = attrs.get("password")
        obj = models.UserInfo.objects.filter(username=username).first()
        if obj:
            raise ValidationError({"error": "该用户已经存在"})
        # 将提交的参数中密码进行加密并替换
        md5_password = md5_.setPassword(password)
        attrs["password"] = md5_password
        # print(attrs)
        return attrs


class LoginSer(serializers.ModelSerializer):
    avatar = serializers.CharField(read_only=True)
    nickname = serializers.CharField(read_only=True)
    campus = serializers.CharField(source="campus.name", read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.UserInfo
        fields = ["username", "password", "avatar", "nickname", "campus"]

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        md5_password = md5_.setPassword(password)
        user = models.UserInfo.objects.filter(username=username, password=md5_password).first()
        if not user:
            raise ValidationError({"error": "用户名或者密码错误"})
        attrs["password"] = md5_password
        # 登录成功，根据用户名和未加密密码 以及配置文件的django盐巴生成jwt密钥
        payload = {
            "username": username,
            "password": password,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60 * 24 * 7)  # 超时时间一个礼拜
        }
        attrs["token"] = get_jwt(payload=payload)
        return attrs


############################  图书相关 #######################################

class BookSer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"
        depth = 1


class TypeSer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = "__all__"


############################  订单相关 #######################################

class OrderSer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.nickname",read_only=True)
    book = serializers.CharField(source="book.name",read_only=True)
    seller = serializers.CharField(source="seller.name",read_only=True)
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = models.Order
        fields = "__all__"
