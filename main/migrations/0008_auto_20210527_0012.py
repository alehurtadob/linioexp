# Generated by Django 3.2 on 2021-05-27 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210522_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='clientes',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='repartidor',
        ),
    ]