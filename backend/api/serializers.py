# backend/api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Restaurant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ('id', 'user', 'date_of_birth', 'city', 'state', 'country', 'nickname')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        customer = Customer.objects.create(user=user, **validated_data)
        return customer
    
class RestaurantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Restaurant
        fields = ('id', 'user', 'name', 'address', 'cuisine_type')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        restaurant = Restaurant.objects.create(user=user, **validated_data)
        return restaurant