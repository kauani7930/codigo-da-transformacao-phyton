from django.test import TestCase
from .models import Produto

class ProdutoTest(TestCase):
    def test_criacao_produto(self):
        produto = Produto.objects.create(
            nome="Celular",
            descricao="Smartphone",
            preco=1200.00,
            quantidade=5
        )
        self.assertEqual(produto.nome, "Celular")
