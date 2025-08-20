from django.contrib import admin
from django.contrib.auth.models import User

from apps.pedido.models import Pedido


class PedidoInline(admin.TabularInline):
    model = Pedido
    fields = ['id', 'itens']
    extra = 0
    show_change_link = True


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'username',
        'email'
    ]
    inlines = [PedidoInline]


admin.site.unregister(User)  # Retira o registro de User padrão
admin.site.register(User, UserAdmin)
