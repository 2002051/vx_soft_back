from django.db import models
import random


# Create your models here.

class UserInfo(models.Model):
    """用户"""
    avatar = models.CharField(verbose_name="头像", max_length=128, default="/media/avatar/default.png")
    nickname = models.CharField(verbose_name="昵称", max_length=128, default=f"用户{random.randint(100000, 999999)}")
    username = models.CharField(verbose_name="用户名", max_length=128)
    password = models.CharField(verbose_name="密码", max_length=255)
    campus = models.ForeignKey(verbose_name="所属校区", to="Campus", on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)


class Session(models.Model):
    """会话，类似于一个聊天室，表示两个人直接的连接关系"""
    sellerid = models.ForeignKey(verbose_name="卖家", related_name='seller', to="UserInfo", on_delete=models.CASCADE)
    buyerid = models.ForeignKey(verbose_name="买家", related_name='buyerid', to="UserInfo", on_delete=models.CASCADE)


class Message(models.Model):
    """消息表"""
    sessionID = models.ForeignKey(verbose_name="会话id", to="Session", on_delete=models.CASCADE)
    senderID = models.ForeignKey(verbose_name="发送者", related_name='sender', to="UserInfo", on_delete=models.CASCADE)
    recipientID = models.ForeignKey(verbose_name="接收者", related_name='ecipient', to="UserInfo",
                                    on_delete=models.CASCADE)
    content = models.TextField(verbose_name="消息内容")
    create_time = models.DateTimeField(verbose_name="发送时间", auto_now_add=True)


class Campus(models.Model):
    """校区"""
    name = models.CharField(verbose_name="校区名称", max_length=100)


class Type(models.Model):
    """二手书类别"""
    title = models.CharField(verbose_name="类别名", max_length=128)


class Book(models.Model):
    """二手书"""
    type = models.ForeignKey(verbose_name="类别", to="Type", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="书名", max_length=128)
    price = models.IntegerField(verbose_name="价格", default=1)
    author = models.CharField(verbose_name="作者", max_length=128)
    image = models.CharField(verbose_name="图片", max_length=128, default="/media/book_img/default.png")
    detail = models.CharField(verbose_name="详情", max_length=255)
    status = models.CharField(verbose_name="使用情况", max_length=128)
    userinfo = models.ForeignKey(verbose_name="发布者", to="UserInfo", on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name="发送时间", auto_now_add=True)


class Cart(models.Model):
    """购物车条目"""
    user = models.ForeignKey(verbose_name="用户", to="UserInfo", on_delete=models.CASCADE)
    book = models.ForeignKey(verbose_name="书籍", to="Book", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="数量", default=1)
    create_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)


class Order(models.Model):
    """订单表"""
    user = models.ForeignKey(verbose_name="用户", related_name="user", to="UserInfo", on_delete=models.CASCADE)
    book = models.ForeignKey(verbose_name="书籍", to="Book", on_delete=models.CASCADE)
    seller = models.ForeignKey(verbose_name="卖家", related_name='order_seller', to="UserInfo", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="数量", default=1)
    address = models.ForeignKey(to="Address", verbose_name="配送地址", related_name="orders", on_delete=models.CASCADE)
    STATUS_CHOICES = (
        (0, '待收货'),
        (1, '已确认'),
        (2, '我的售卖'),
    )
    status = models.IntegerField(verbose_name="订单状态", choices=STATUS_CHOICES, default=0)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)


class Address(models.Model):
    """地址表"""
    userinfo = models.ForeignKey(verbose_name="用户", to="UserInfo", on_delete=models.CASCADE, default=1)
    receiver_name = models.CharField(verbose_name="收件人姓名", max_length=100)
    phone_number = models.CharField(verbose_name="联系电话", max_length=20)
    campus = models.ForeignKey(verbose_name="校区", to="Campus", on_delete=models.CASCADE,default=1)
    is_default = models.BooleanField(verbose_name="是否默认地址", default=False)
    detail = models.TextField(verbose_name="配送说明", blank=True, null=True)

# class Article(models.Model):
#     """帖子"""
#     pass

# class Followers(models.Model):
#     """用户关注关系表"""
#     follower_id = models.ForeignKey(verbose_name="关注者id", to=UserInfo, on_delete=models.CASCADE)
#     following_id = models.ForeignKey(verbose_name="被关注者id", to=UserInfo, on_delete=models.CASCADE)
#     create_time = models.DateTimeField(verbose_name="关注时间", auto_now_add=True)
