# Generated by Django 3.2 on 2021-05-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20210508_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='order_api_key',
            field=models.CharField(max_length=24, verbose_name='Order API_KEY'),
        ),
        migrations.AlterField(
            model_name='account',
            name='order_api_secret',
            field=models.CharField(max_length=48, verbose_name='Order API_SECRET'),
        ),
        migrations.AlterField(
            model_name='account',
            name='order_cancel_api_key',
            field=models.CharField(max_length=24, verbose_name='Order Cancel API_KEY'),
        ),
        migrations.AlterField(
            model_name='account',
            name='order_cancel_api_secret',
            field=models.CharField(max_length=48, verbose_name='Order Cancel API_SECRET'),
        ),
    ]