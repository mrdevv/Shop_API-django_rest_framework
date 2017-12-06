from django.contrib import admin
from .models import CustomerProfile, Order, Stock, Shop, Product

# Register your models here.

admin.site.register(CustomerProfile)
admin.site.register(Order)
admin.site.register(Stock)
admin.site.register(Shop)
admin.site.register(Product)