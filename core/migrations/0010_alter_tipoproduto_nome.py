# Generated by Django 4.1.6 on 2023-02-24 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_tipoproduto_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproduto',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]