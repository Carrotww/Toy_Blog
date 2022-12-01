from django.urls import path, re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi()),
    # path('chat/<int:room_id>', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/notification/(?P<center_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]