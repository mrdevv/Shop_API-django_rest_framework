from rest_framework import serializers
from .models import Product, Shop, Stock, Order, CustomerProfile


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['username', 'password']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ('username', 'password', 'first_name', 'email')

    def create(self, validated_data):
        user = super(UserRegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ('password',)

    def update(self, instance, validated_data):
        user = super(UserUpdatePasswordSerializer, self).update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ('email', 'first_name', 'last_name')



class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


