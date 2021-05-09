from django.contrib import admin

from base.models import Account


class account(admin.ModelAdmin):
    search_fields = ['name', ]


admin.site.register(Account, account)