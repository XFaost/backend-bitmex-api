import websockets
import json


def get_wb():
    return websockets.connect("wss://www.bitmex.com/realtime?subscribe=instrument:XBTUSD")


def abstract_subscribe_mess(data):
    data = json.loads(data)
    abstract_data = {}

    try:
        abstract_data['timestamp'] = data['data'][0]['timestamp']
        abstract_data['account'] = '_account'
        abstract_data['symbol'] = data['data'][0]['symbol']
        abstract_data['price'] = data['data'][0]['lastPrice']
    except Exception as e:
        return None

    return json.dumps(abstract_data)
