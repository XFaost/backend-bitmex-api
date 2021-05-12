from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name', null=True)

    api_key = models.CharField(max_length=24, verbose_name='Order API_KEY')
    api_secret = models.CharField(max_length=48, verbose_name='Order API_SECRET')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Accounts'
        db_table = 'account'


class Order(models.Model):
    orderID = models.CharField(max_length=36)
    symbol = models.CharField(max_length=25)
    volume = models.FloatField()
    timestamp = models.DateTimeField()
    side = models.CharField(max_length=4)
    price = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.orderID

    class Meta:
        verbose_name_plural = 'Orders'
        db_table = 'order'
