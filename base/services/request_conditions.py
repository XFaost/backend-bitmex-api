from base.models import Account


class IRequestConditions:
    def check(self, request):
        pass


class IsAuth(IRequestConditions):
    def __init__(self):
        self.__next = None

    def check(self, request):
        if request.user and request.user.is_authenticated:
            if self.__next:
                return self.__next.check(request)
            else:
                return self.__all_ok()
        return self.__please_log_in()

    def set_next(self, next: IRequestConditions):
        self.__next = next

    def __all_ok(self):
        return {'status': 201}

    def __please_log_in(self):
        return {'status': 403, 'message': 'Please log in'}


class CheckAccount(IRequestConditions):
    def __init__(self):
        self.__next = None

    def check(self, request):
        name = request.GET.get('account', None)
        if name:
            if Account.objects.filter(name=name).first():
                if self.__next:
                    return self.__next.check(request)
                else:
                    return self.__all_ok()
            return self.__account_not_found()
        return self.__please_enter_account_name()

    def set_next(self, next: IRequestConditions):
        self.__next = next

    def __all_ok(self):
        return {'status': 201}

    def __please_enter_account_name(self):
        return {'status': 403, 'message': 'Please enter account name'}

    def __account_not_found(self):
        return {'status': 403, 'message': 'Account not found'}


def check_for_request_conditions(request):
    is_auth = IsAuth()
    check_account = CheckAccount()

    is_auth.set_next(check_account)
    return is_auth.check(request)