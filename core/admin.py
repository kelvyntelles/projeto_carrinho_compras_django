from django.contrib import admin
from .models import Produto, Pedido, TipoProduto, ItemPedido


admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(TipoProduto)
admin.site.register(ItemPedido)

