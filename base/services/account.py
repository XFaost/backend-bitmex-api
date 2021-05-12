from bitmex import bitmex
from base.models import Account


def get_name_account_from_request(request):
    return request.GET.get('account', None)


def get_account_by_name(name):
    return Account.objects.filter(name=name).first()


def get_account(request):
    name = get_name_account_from_request(request)
    return get_account_by_name(name)


def get_client_by_account(account):
    return bitmex(True, None, account.api_key, account.api_secret)


def get_client(request):
    account = get_account(request)
    return get_client_by_account(account)
