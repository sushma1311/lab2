# admin.py

from django.contrib import admin
from .models import Restaurant, Customer  # Import your models

# Register your models
admin.site.register(Restaurant)
admin.site.register(Customer)
