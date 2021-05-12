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
