"""
ASGI config for soft project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soft.settings')
from channels.routing import ProtocolTypeRouter, URLRouter
from .routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application

# application = get_asgi_application()


application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # 如果是http协议那么就会使用get_asgi_application()
    "websocket": URLRouter(websocket_urlpatterns),  # 可以指定websocket 相应的路由
})
