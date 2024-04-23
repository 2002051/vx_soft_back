# wbsocket协议 处理买家和卖家的聊天信息
import json
import os
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from tranapp import models

from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from tranapp.utils.res_ import MyResponse
from tranapp.utils.auth_ import LoginAuth
from tranapp.utils.ser_ import MessageSer

Session_DICT = {}


class ChatRoom(WebsocketConsumer):
    """聊天消息处理"""

    def websocket_connect(self, message):
        # print(self.scope) #请求参数
        buyer = self.scope["url_route"]["kwargs"].get("buyer")
        seller = self.scope["url_route"]["kwargs"].get("seller")
        # 尝试创建一个会话 ,这里session表设计的有点问题，buyerid字段指向的是一个实例，所以需要使用buyerid_id来写入id
        session_obj = models.Session.objects.filter(buyerid_id=buyer, sellerid_id=seller).first()
        if not session_obj:
            session_obj = models.Session.objects.create(buyerid_id=buyer, sellerid_id=seller)
        # 在内存中写入当前会话
        Session_DICT.setdefault(session_obj.id, [])  # 如果对应聊天室不存在默认创建一个空列表
        Session_DICT[session_obj.id].append(self)  # 将当前连接实例对象加入到对应session中，然后后续可以遍历之以广播消息

        self.accept()

    def websocket_receive(self, message):
        """我总结一下思路
                首先 url中可以获取到参数，根据这个参数得到对应的session信息
                然后前端发送的消息，携带对应发送人的id，这三者就可以存入消息记录表了。
                再根据session 去内存中找对应的聊天组，并把处理好的数据广播给他们
        """
        buyer = self.scope["url_route"]["kwargs"].get("buyer")
        seller = self.scope["url_route"]["kwargs"].get("seller")
        session_obj = models.Session.objects.filter(buyerid_id=buyer, sellerid_id=seller).first()
        """
        前端需要对数据格式化 ， sender 表示发送者的id
        var msg = JSON.stringify({"sender":1,"data":"123123"})
        ws.send(msg)
        # 后端拿到json字符串
        接收到消息了 {'type': 'websocket.receive', 'text': '{"sender":1,"data":"123123"}'}
        """
        data = json.loads(message["text"])
        sender = data.get("sender")
        msg = data.get("data")
        # 创建一条消息记录
        recipientID = seller if sender == buyer else buyer  # 如果发送者id 和购买者一致，那么接收者就是另一个人
        message_obj = models.Message.objects.create(sessionID_id=session_obj.id, senderID_id=sender,
                                                    recipientID_id=recipientID, content=msg)

        # 获取发送者的信息
        userinfo = models.UserInfo.objects.filter(id=sender).first()
        result = {"user_id": userinfo.id, "avatar": userinfo.avatar, "msg": message_obj.content}
        # 广播消息
        for client in Session_DICT[session_obj.id]:
            client.send(text_data=json.dumps(result))

    def websocket_disconnect(self, message):
        print("客户端断开连接了")
        raise StopConsumer()


class MessageView(MyResponse, APIView):
    authentication_classes = [LoginAuth]

    def get(self, request):
        user = request.user
        session_id = int(request.query_params.get("session_id"))
        # 一个聊天会话的记录，要满足会话id对应，同时当前登录用户是其中的发送者，防止其它用户可以看到
        queryset = models.Message.objects.filter(sessionID_id=session_id).filter(
            Q(senderID_id=user.id) | Q(recipientID_id=user.id))
        page = LimitOffsetPagination()
        ser = MessageSer(instance=queryset, many=True)
        ser2 = MessageSer(page.paginate_queryset(queryset, self.request, view=None),many=True)
        return page.get_paginated_response(ser2.data)

        # return Response(ser.data)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
