# Generated by Django 5.1.4 on 2025-01-20 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_qty',
        ),
    ]
