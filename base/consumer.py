from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from base.services.account import get_account_by_name
from base.services.subscribe import BitMexSubscribe


class ChatConsumer(WebsocketConsumer):

    def __init__(self):
        super(ChatConsumer, self).__init__()
        print('__init__')

    def connect(self):
        print('connect')
        self.accept()

    def disconnect(self, close_code):
        print('disconnect')

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print('receive')
        print(text_data_json)
        account = get_account_by_name(text_data_json['name'])
        print(account)

        self.ws = BitMexSubscribe(account.api_key, account.api_secret)
        self.send('{"mess": "1"}')
        async_to_sync(self.send_data())
        #self.send_data()

    #def send_data(self):
    async def send_data(self):
        print('send_data')
        mess = self.ws.get_abstract_mess()
        if mess:
            self.send(mess)
        self.send_data()
