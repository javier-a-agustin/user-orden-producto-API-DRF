from rest_framework import serializers
 
from .models import Product, Order, OrderDescription

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):

        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class OrderDescriptionSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = OrderDescription
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
