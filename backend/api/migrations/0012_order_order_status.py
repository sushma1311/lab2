# Generated by Django 4.2.16 on 2024-10-26 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_address_order_delivery_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('New', 'New'), ('Preparing', 'Preparing'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='New', max_length=20),
        ),
    ]