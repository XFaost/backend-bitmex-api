from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio as aio

from base.services.subscribe import get_wb, abstract_subscribe_mess


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        ws = await get_wb()
        while True:
            if not ws.open:
                print('Reconnecting...')
                ws = await get_wb()
            try:
                data = await aio.wait_for(ws.recv(), timeout=20)
            except aio.TimeoutError:
                try:
                    pong_waiter = await ws.ping()
                    await aio.wait_for(pong_waiter, timeout=10)
                except aio.TimeoutError:
                    break
                    print('Timeout')
            except Exception as e:
                print(e)
            else:
                abstract_data = abstract_subscribe_mess(data)
                if abstract_data:
                    print(abstract_data)
                    await self.send(abstract_data)

        print('End')


            # for i in range(1000):
            #     await self.send(json.dumps({'timestamp': i, 'account': '_account', 'symbol': '_symbol', 'price': '_price'}))
            #     print(i)
            #     await sleep(5)
