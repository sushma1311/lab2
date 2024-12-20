# Generated by Django 4.2.16 on 2024-10-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_restaurant_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('Appetizer', 'Appetizer'), ('Salad', 'Salad'), ('Main Course', 'Main Course'), ('Dessert', 'Dessert'), ('Beverage', 'Beverage')], default='Main Course', max_length=50),
        ),
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredients',
            field=models.TextField(default='Ingredients not specified'),
        ),
    ]
