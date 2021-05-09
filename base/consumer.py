from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asyncio import sleep


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        #self.send(json.dumps({'timestamp': 1, 'account': '_account', 'symbol': '_symbol', 'price': '_price'}))
        for i in range(1000):
            await self.send(json.dumps({'timestamp': i, 'account': '_account', 'symbol': '_symbol', 'price': '_price'}))
            print(i)
            await sleep(5)
