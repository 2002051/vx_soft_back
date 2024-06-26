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


class EditUserSer(serializers.ModelSerializer):
    """编辑信息序列化器"""
    username = serializers.CharField(allow_blank=True, required=False)
    password = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = models.UserInfo
        fields = "__all__"


class LoginSer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    avatar = serializers.CharField(read_only=True)
    nickname = serializers.CharField(read_only=True)
    # campus = serializers.CharField(source="campus.name", read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.UserInfo
        fields = ["id", "username", "password", "avatar", "nickname", "campus"]
        depth = 1

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


class CampusSer(serializers.ModelSerializer):
    class Meta:
        model = models.Campus
        fields = "__all__"


############################  图书相关 #######################################

class BookSer(serializers.ModelSerializer):
    """书籍序列化器"""
    type_id = serializers.IntegerField(write_only=True)
    active_dict = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Book
        fields = "__all__"
        depth = 1

    def get_active_dict(self, obj):
        return {
            obj.active,
            obj.get_active_display(),
        }


class TypeSer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = "__all__"


############################  订单相关 #######################################

class OrderSer(serializers.ModelSerializer):
    """订单序列化器"""
    # status = serializers.CharField( read_only=True)
    # status_text = serializers.CharField(source="get_status_display", read_only=True)
    status_dict = serializers.SerializerMethodField(read_only=True)
    address_id = serializers.IntegerField(write_only=True)
    seller_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField()
    status = serializers.IntegerField(allow_null=True, write_only=True)

    class Meta:
        model = models.Order
        fields = "__all__"
        depth = 2

    def get_status_dict(self, obj):
        return {
            obj.status,
            obj.get_status_display(),
        }


class AddressSer(serializers.ModelSerializer):
    """地址序列化器"""

    campus_id = serializers.IntegerField(write_only=True)
    is_default = serializers.BooleanField()

    class Meta:
        model = models.Address
        fields = "__all__"
        depth = 1  # 一级深度查询外键，如果懒得定制字段可以这样，但会略微影响效率


############################  消息相关 #######################################

class MessageSer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"
        depth = 1


class SessionSer(serializers.ModelSerializer):
    class Meta:
        model = models.Session
        fields = "__all__"
        depth = 1


################################  购物车相关  #####################################
class CartSer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.Cart
        fields = "__all__"
        depth = 1


############################# 帖子 ####################################

class ArticlSer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"
        depth = 1


class ArticlCommentSer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleComment
        fields = "__all__"
        depth = 1


class ArticlCommentSer2(serializers.ModelSerializer):
    article_id = serializers.IntegerField()
    sender_id = serializers.IntegerField()

    class Meta:
        model = models.ArticleComment
        fields = ["article_id", "sender_id", "content"]
        depth = 1


################################  其它  #####################################


class BannerSer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = "__all__"
