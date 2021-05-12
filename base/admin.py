from django.contrib import admin

from base.models import Account, Order


class account(admin.ModelAdmin):
    search_fields = ['name', ]


class order(admin.ModelAdmin):
    search_fields = ['orderID', ]


admin.site.register(Account, account)
admin.site.register(Order, order)
