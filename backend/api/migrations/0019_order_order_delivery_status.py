# Generated by Django 4.2.16 on 2024-10-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_delivery_status',
            field=models.CharField(choices=[('order received', 'order received'), ('preparing', 'preparing'), ('on the way', 'on the way'), ('pick up ready', 'pick up ready'), ('delivered', 'delivered'), ('picked up', 'picked up')], default='order received', max_length=20),
        ),
    ]
