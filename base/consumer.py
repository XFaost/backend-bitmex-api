from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        #self.send(json.dumps({'timestamp': 1, 'account': '_account', 'symbol': '_symbol', 'price': '_price'}))
        for i in range(1000):
            self.send(json.dumps({'timestamp': i, 'account': '_account', 'symbol': '_symbol', 'price': '_price'}))
            print(i)
            sleep(5)
