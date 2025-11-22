from django.contrib import admin
from .models import Item, Order, OrderItem

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'price_in_dollars')
    search_fields = ('name',)

    def price_in_dollars(self, obj):
        return f"${obj.price / 100:.2f}"
    price_in_dollars.short_description = "Price"

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'total_price', 'paid')
    list_filter = ('paid', 'created_at')
    inlines = [OrderItemInline]

    def total_price(self, obj):
        return f"${obj.get_total_price():.2f}"