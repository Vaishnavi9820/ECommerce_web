# Generated by Django 4.2.2 on 2023-06-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
