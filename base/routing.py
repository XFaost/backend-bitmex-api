from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/subscribes', consumers.ChatConsumer.as_asgi(), name="subscribes",),
]