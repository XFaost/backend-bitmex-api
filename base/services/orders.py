import json

from base.models import Order
from base.services.account import get_client, get_account
from base.services.request_conditions import check_for_request_conditions


def create_order(request):
    result = check_for_request_conditions(request)
    if result['status'] != 201:
        return result

    client = get_client(request)

    try:
        data = client.Order.Order_new(**request.data).result()[0]
        Order.objects.get_or_create(
            account = get_account(request),
            orderID = data['orderID'],
            symbol = data['symbol'],
            volume = data['orderQty'],
            timestamp = data['timestamp'],
            side = data['side'],
            price = data['price']
        )
        return data
    except Exception as e:
        return __get_except_mess(e)


def view_active_orders(request):
    result = check_for_request_conditions(request)
    if result['status'] != 201:
        return result

    client = get_client(request)

    try:
        return client.Order.Order_getOrders(filter=json.dumps({"open": True})).result()[0]
    except Exception as e:
        return __get_except_mess(e)


def view_active_order(request, order_id):
    result = check_for_request_conditions(request)
    if result['status'] != 201:
        return result

    client = get_client(request)

    try:
        return client.Order.Order_getOrders(filter=json.dumps({"orderID": order_id})).result()[0]
    except Exception as e:
        return __get_except_mess(e)


def delete_order(request, order_id):
    result = check_for_request_conditions(request)
    if result['status'] != 201:
        return result

    client = get_client(request)

    try:
        Order.objects.filter(orderID=order_id).delete()
        return client.Order.Order_cancel(orderID=order_id).result()[0]
    except Exception as e:
        return __get_except_mess(e)


def __get_except_mess(e):
    return {'message': str(e)}
