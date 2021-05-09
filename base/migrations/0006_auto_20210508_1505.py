# Generated by Django 3.2 on 2021-05-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210507_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='api_key',
        ),
        migrations.RemoveField(
            model_name='account',
            name='api_secret',
        ),
        migrations.AddField(
            model_name='account',
            name='order_api_key',
            field=models.CharField(max_length=24, null=True, verbose_name='Order API_KEY'),
        ),
        migrations.AddField(
            model_name='account',
            name='order_api_secret',
            field=models.CharField(max_length=48, null=True, verbose_name='Order API_SECRET'),
        ),
        migrations.AddField(
            model_name='account',
            name='order_cancel_api_key',
            field=models.CharField(max_length=24, null=True, verbose_name='Order Cancel API_KEY'),
        ),
        migrations.AddField(
            model_name='account',
            name='order_cancel_api_secret',
            field=models.CharField(max_length=48, null=True, verbose_name='Order Cancel API_SECRET'),
        ),
    ]
