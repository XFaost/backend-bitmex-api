import hashlib
import hmac
import json
import time
import urllib

from websocket import create_connection

from base.services.account import get_account_by_name


class BitMexSubscribe:
    __BITMEX_URL = "wss://testnet.bitmex.com"

    __VERB = "GET"
    __ENDPOINT = "/realtime"

    def __init__(self, account_name):
        self.account_name = account_name
        account = get_account_by_name(account_name)
        API_KEY = account.api_key
        API_SECRET = account.api_secret

        expires = int(time.time()) + 5
        signature = self.__bitmex_signature(API_SECRET, self.__VERB, self.__ENDPOINT, expires)
        self.ws = create_connection(self.__BITMEX_URL + self.__ENDPOINT)
        print("Receiving Welcome Message...")
        result = self.get_mess()
        print("Received '%s'" % result)

        request = {"op": "authKeyExpires", "args": [API_KEY, expires, signature]}
        self.ws.send(json.dumps(request))
        print("Sent Auth request")
        result = self.get_mess()
        print("Received '%s'" % result)

        request = {"op": "subscribe", "args": "instrument"}
        self.ws.send(json.dumps(request))
        print("Sent subscribe")
        result = self.get_mess()
        print("Received '%s'" % result)
        result = self.get_mess()
        print("Received '%s'" % result)

    def get_mess(self):
        return self.ws.recv()

    def __bitmex_signature(self, apiSecret, verb, url, nonce, postdict=None):
        """Given an API Secret key and data, create a BitMEX-compatible signature."""
        data = ''
        if postdict:
            # separators remove spaces from json
            # BitMEX expects signatures from JSON built without spaces
            data = json.dumps(postdict, separators=(',', ':'))
        parsedURL = urllib.parse.urlparse(url)
        path = parsedURL.path
        if parsedURL.query:
            path = path + '?' + parsedURL.query
        # print("Computing HMAC: %s" % verb + path + str(nonce) + data)
        message = (verb + path + str(nonce) + data).encode('utf-8')
        print("Signing: %s" % str(message))

        signature = hmac.new(apiSecret.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
        print("Signature: %s" % signature)
        return signature

    def get_abstract_mess(self):
        data = json.loads(self.get_mess())
        abstract_data = {}

        try:
            abstract_data['timestamp'] = data['data'][0]['timestamp']
            abstract_data['account'] = self.account_name
            abstract_data['symbol'] = data['data'][0]['symbol']
            abstract_data['price'] = data['data'][0]['lastPrice']
        except Exception as e:
            return None

        return json.dumps(abstract_data)
