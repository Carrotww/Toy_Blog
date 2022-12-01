import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import chats.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testpro.settings")	# mysite 는 django 프로젝트 이름
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.

application = ProtocolTypeRouter({
    # 서버 연결시 protocaltyperouter 가 연결의 종류를 탐색
  "http": get_asgi_application(),
  # http일 시 get_asgi_application 실행
  "websocket": AuthMiddlewareStack(
            URLRouter(
                chats.routing.websocket_urlpatterns	# chat 은 routing.py 가 들어있는 앱 이름
            )
        )
})