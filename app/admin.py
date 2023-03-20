from django.contrib import admin
from .models import Product, Cart, Customer, OrderPlaced

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["id", "title", "selling_price", "discounted_price", "description" ,"brand",
    "category",'product_image']

@admin.register(Cart)
class CartAdmin( admin.ModelAdmin):
    list_display=["id", "user", "quantity", 'product']

@admin.register(Customer)
class CustomerAdmin( admin.ModelAdmin):
    list_display=["id", "user",'name', "locality","city", "state","zipcode","phone_number"]

@admin.register(OrderPlaced)
class OrderplacedAdmin(admin.ModelAdmin):
    list_display=["id", "user","customer","product","quantity","status","ordered_date"]