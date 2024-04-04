from django.contrib import admin
from .models import Client, Item, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_filter = ['name', 'phone']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя(клиента)'


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity']
    list_filter = ['name', 'add_data']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Название продукта(name)'
    actions = [reset_quantity]
    fieldsets = [
        ('Название и описание',
         {
             'fields':  ['name', 'description']
         }
         ),
        ('Бухгалтерия',
         {
             'fields':  ['price', 'quantity']
         }
         ),
        ('Прочее',
         {
             'fields':  ['add_data', 'image']
         }
         )
    ]
    readonly_fields = ['add_data']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_sum', 'date', 'client']
    list_filter = ['client', 'date']
    search_fields = ['total_sum']
    search_help_text = 'Поиск по полю Сумме заказа(total_sum)'


admin.site.register(Client, ClientAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
