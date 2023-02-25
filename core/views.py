from django.shortcuts import render, redirect
from .models import Produto, ItemPedido, Pedido


def getTotalItensPedido():
    itens = ItemPedido.objects.all()
    tota_itens = len(itens)
    return tota_itens


def addItemPedido(request, id):
    produto = Produto.objects.get(id=id)
    ItemPedido.objects.create(preco_unitario=produto.preco, quantidade=1, preco_total=produto.preco, produto=produto)

    return redirect(home)


def delItemPedido(request, id):
    item = ItemPedido.objects.get(id=id)
    item.delete()

    return redirect(carrinho)


def home(request):
    total_itens_pedido = getTotalItensPedido()
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos, 'total_itens_pedido': total_itens_pedido})


def totalPedido():
    itens = ItemPedido.objects.all()

    total = 0

    for item in itens:
        total += item.preco_unitario

    return total


def carrinho(request):
    total_pedido = totalPedido()
    itens = ItemPedido.objects.all()
    return render(request, 'carrinho.html', {'itens': itens, 'total_pedido': total_pedido})


def finalizarPedido(request):
    nome = request.POST.get("nome_cliente")
    valor_total = totalPedido()
    Pedido.objects.create(nome_cliente=nome, valor_total=valor_total)

    itens = ItemPedido.objects.all()

    itens.delete()

    return redirect(pedido)


def pedido(request):
    return render(request, 'pedido.html')
