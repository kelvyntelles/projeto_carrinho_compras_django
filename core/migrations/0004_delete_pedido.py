# Generated by Django 4.1.6 on 2023-02-24 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pedido_nome'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]