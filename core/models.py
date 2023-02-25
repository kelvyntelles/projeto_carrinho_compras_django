from django.db import models


class TipoProduto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    preco = models.FloatField()
    img_url = models.CharField(max_length=300)
    tipo_produto = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class ItemPedido(models.Model):
    preco_unitario = models.FloatField()
    quantidade = models.IntegerField()
    preco_total = models.FloatField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produto.nome} - " \
               f"{self.produto.descricao} - " \
               f"{self.quantidade} - " \
               f"{self.preco_total}"


class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=100)
    valor_total = models.FloatField()
    itens = models.ManyToManyField(ItemPedido)

    def __str__(self):
        return self.nome_cliente

