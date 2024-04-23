from django.urls import path
from tranapp.views import wbchat

websocket_urlpatterns = [
    path("chat/<int:buyer>/<int:seller>/", wbchat.ChatRoom.as_asgi())
]
