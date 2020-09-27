from django.contrib import admin

from shop.models import Product, Tag, Cart, Review, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = []
    # list_filter = []
    # search_fields = []
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # list_display = []
    # list_filter = []
    # search_fields = []
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # list_display = []
    # list_filter = []
    # search_fields = []
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # list_display = []
    # list_filter = []
    # search_fields = []
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display = []
    # list_filter = []
    # search_fields = []
    pass
