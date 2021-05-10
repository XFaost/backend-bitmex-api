from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('connect')
        self.accept()

    def disconnect(self, close_code):
        print('disconnect')

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print('receive')
        print(text_data_json)

# from channels.generic.websocket import AsyncWebsocketConsumer
# import codecs
# import hashlib
# import hmac
# import json
# import time
# import urllib
# import uuid
# from websocket import create_connection
# from asgiref.sync import sync_to_async
#
# from base.models import Account
#
# BITMEX_URL = "wss://testnet.bitmex.com"
#
# VERB = "GET"
# AUTH_ENDPOINT = "/realtime"
# ENDPOINT = "/realtimemd?transport=websocket&b64=1"
#
# KEYS = {
#     "vVKkYKb4QLnFoGvMHq_And9Z": "mCyT7h23tDw2BSNVVP9NX28Lq8-R-9bq3SMD9LYRwFlfRp4g",
#     "48GphC_MTWN_0ntW4V1osU4S": "-hoVHM9kC1JRwlQBPjYdzosCCpKl7CNtomzyCTGVoLcQ5PSV"
# }
#
#
# class WSConsumer(AsyncWebsocketConsumer):
#
#     def __init__(self):
#         super(WSConsumer, self).__init__()
#         self.ws = create_connection(BITMEX_URL + ENDPOINT)
#
#     async def connect(self):
#         print('connect')
#         self.accept()
#         await self.add_subscription_for_account('my')
#
#     async def disconnect(self, code):
#         print('disconnect')
#
#     async def receive(self, text_data=None, bytes_data=None):
#         text_data_json = json.loads(text_data)
#         action = text_data_json['action']
#         account = text_data_json['account']
#         print('receive: ' + text_data)
#
#     async def send_mess(self, mess):
#         self.send(mess)
#
#     async def wait_for_bitmex_data(self):
#         pass
#
#     async def add_subscription_for_account(self, account_name):
#         print('add_subscription_for_account')
#         account = Account.objects.filter(name=account_name).first()
#         key = account.api_key
#         secret = account.api_secret
#         # key = "vVKkYKb4QLnFoGvMHq_And9Z"
#         # secret = "mCyT7h23tDw2BSNVVP9NX28Lq8-R-9bq3SMD9LYRwFlfRp4g"
#
#         nonce = int(round(time.time() * 1000))
#         signature = self.bitmex_signature(secret, VERB, AUTH_ENDPOINT, nonce)
#         connID = self.random_id()
#         channelName = "userAuth:" + key + ":" + str(nonce) + ":" + signature
#         request = [1, connID, channelName]
#         print(json.dumps(request))
#         self.ws.send(json.dumps(request))
#
#         request = [0, connID, channelName, {'op': 'authKey', 'args': [key, nonce, signature]}]
#         print('sending auth request: {}'.format(json.dumps(request)))
#         self.ws.send(json.dumps(request))
#
#         # Send a request that requires authorization on this multiplexed connection.
#         op = {"op": "subscribe", "args": "instrument"}
#         request = [0, connID, channelName, op]
#         self.ws.send(json.dumps(request))
#
#     def bitmex_signature(self, apiSecret, verb, url, nonce, postdict=None):
#         """Given an API Secret and data, create a BitMEX-compatible signature."""
#         data = ''
#         if postdict:
#             # separators remove spaces from json
#             # BitMEX expects signatures from JSON built without spaces
#             data = json.dumps(postdict, separators=(',', ':'))
#         parsedURL = urllib.parse.urlparse(url)
#         path = parsedURL.path
#         if parsedURL.query:
#             path = path + '?' + parsedURL.query
#         # print("Computing HMAC: %s" % verb + path + str(nonce) + data)
#         message = (verb + path + str(nonce) + data).encode('utf-8')
#
#         signature = hmac.new(apiSecret.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
#         return signature
#
#     # Generates a random ID.
#     def random_id(self):
#         return codecs.encode(uuid.uuid4().bytes, 'base64').rstrip(b'=\n').decode('utf-8')
