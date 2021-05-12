from channels.generic.websocket import WebsocketConsumer
import json
import threading

from base.services.subscribe import BitMexSubscribe


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print('connect')
        self.accept()

    def disconnect(self, close_code):
        print('disconnect')
        self.close()
        self.ws = None

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print('receive')
        print(text_data_json)
        try:
            if text_data_json['action'] == 'subscribe':
                self.ws = BitMexSubscribe(text_data_json['account'])
                self.my_thread = threading.Thread(target=self.read)
                self.my_thread.start()
            elif text_data_json['action'] == 'unsubscribe':
                self.ws = None
        except:
            pass

    def read(self):

        while self.ws:
            mess = self.ws.get_abstract_mess()
            if mess:
                print(mess)
                self.send(mess)
