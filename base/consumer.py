from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio as aio
from asyncio import sleep
import websockets


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            ws = await websockets.connect("wss://www.bitmex.com/realtime?subscribe=liquidation:XBTUSD,liquidation:ETHUSD")
            try:
                data = await aio.wait_for(ws.recv(), timeout=20)
            except aio.TimeoutError:
                try:
                    pong_waiter = await ws.ping()
                    await aio.wait_for(pong_waiter, timeout=10)
                except aio.TimeoutError:
                    break
            except Exception as e:
                print(e)
            else:
                print('.', end='', flush=True)
                print(data)

            # for i in range(1000):
            #     await self.send(json.dumps({'timestamp': i, 'account': '_account', 'symbol': '_symbol', 'price': '_price'}))
            #     print(i)
            #     await sleep(5)
