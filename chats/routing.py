from django.urls import path
from django.urls import re_path
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    path('chat/<str:room_name>', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/notification/(?P<center_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]