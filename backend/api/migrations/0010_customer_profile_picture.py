# Generated by Django 4.2.16 on 2024-10-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_restaurant_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='customer_profiles/'),
        ),
    ]
