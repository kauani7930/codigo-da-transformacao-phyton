import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    # Testes de soma
    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 3), 5)
        self.assertEqual(self.calc.soma(-1, 1), 0)

    # Testes de subtração
    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(10, 5), 5)
        self.assertEqual(self.calc.subtracao(0, 7), -7)

    # Testes de multiplicação
    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(4, 3), 12)
        self.assertEqual(self.calc.multiplicacao(-2, 5), -10)

    # Testes de divisão
    def test_divisao(self):
        self.assertEqual(self.calc.divisao(10, 2), 5)
        self.assertAlmostEqual(self.calc.divisao(7, 3), 2.3333, places=4)

    # Teste de divisão por zero
    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divisao(5, 0)

if __name__ == "__main__":
    unittest.main()
