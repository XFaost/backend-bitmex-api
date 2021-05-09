from bitmex import bitmex
from base.models import Account


def get_name_account_from_request(request):
    return request.GET.get('account', None)


def get_account(request):
    name = get_name_account_from_request(request)
    return Account.objects.filter(name=name).first()


def get_client_by_account(account, key_permissions):
    """
    key_permissions:
    * 0 - Order
    * 1 - Order Cancel
    """

    api_key = None
    api_secret = None

    if key_permissions == 0:
        api_key = account.order_api_key
        api_secret = account.order_api_secret
    elif key_permissions == 1:
        api_key = account.order_cancel_api_key
        api_secret = account.order_cancel_api_secret

    if api_key and api_secret:
        return bitmex(True, None, api_key, api_secret)

    return None


def get_client(request, key_permissions):
    account = get_account(request)
    return get_client_by_account(account, key_permissions)
