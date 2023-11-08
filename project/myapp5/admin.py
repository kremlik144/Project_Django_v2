from django.contrib import admin
from .models import Product, Client, Order


@admin.action(description="Очистить таблицу")
def clear_table(modeladmin, request, queryset):
    Client.all().delete()

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'register_date']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name', 'email', 'address']
    search_help_text = 'Поиск по полям Name, Email, Address клиента'
    readonly_fields = ['register_date']
    actions = [clear_table]
    fieldsets = [
        (
            'Имя клиента',
            {
                'classes': 'wide',
                'fields': ['name'],
            }
        ),
        (
            'Данные',
            {
                'fields': ['email', 'phone', 'address'],
            }
        ),
        (
            'Дата регистрации',
            {
                'fields': ['register_date'],
            }
        ),
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount', 'create_date']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени товара'
    readonly_fields = ['register_date']
    readonly_fields = ['create_date']
    fieldsets = [
        (
            'Наименование товара',
            {
                'classes': 'wide',
                'fields': ['name'],
            }
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'amount'],
            }
        ),
        (
            'Дата создания',
            {
                'fields': ['create_date'],
            }
        ),
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_price', 'order_date']
    ordering = ['order_date', 'client']
    list_filter = ['order_date']
    fields = ['client', 'products', 'total_price', 'order_date']
    readonly_fields = ['order_date']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
