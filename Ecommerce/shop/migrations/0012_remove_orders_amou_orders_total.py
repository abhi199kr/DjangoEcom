# Generated by Django 4.0.5 on 2022-07-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_orders_amount_orders_amou'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amou',
        ),
        migrations.AddField(
            model_name='orders',
            name='total',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
