import unittest
from src.o_primeiro_do_ranking import o_primeiro_do_ranking


class TestOPrimeiroDoRanking(unittest.TestCase):

    def test_deve_retornar_posicoes_quando_classificacao_e_pequena(self):
        qtd_pontuacoes = 7
        pontuacoes = [100, 100, 50, 40, 40, 20, 10]
        qtd_pontuacoes_do_joaozinho = 4
        pontuacoes_do_joaozinho = [5, 25, 50, 120]
        resposta = o_primeiro_do_ranking(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho)
        self.assertEqual([6, 4, 2, 1], resposta)
