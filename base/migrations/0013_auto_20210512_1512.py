# Generated by Django 3.2.2 on 2021-05-12 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_order_side'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
    ]
