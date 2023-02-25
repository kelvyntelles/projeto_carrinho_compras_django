from django.urls import path
from .views import home, addItemPedido, carrinho, delItemPedido, finalizarPedido, pedido

urlpatterns = [
    path('', home),
    path('addItemPedido/<int:id>', addItemPedido, name="addItemPedido"),
    path('carrinho/', carrinho),
    path('delItemPedido/<int:id>', delItemPedido, name="delItemPedido"),
    path('finalizarPedido/', finalizarPedido, name="finalizarPedido"),
    path('pedido/', pedido)
]
