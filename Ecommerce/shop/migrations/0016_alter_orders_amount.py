# Generated by Django 4.0.5 on 2022-08-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
