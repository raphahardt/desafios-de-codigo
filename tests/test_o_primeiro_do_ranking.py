# encoding: utf-8

import time
import unittest
from src.o_primeiro_do_ranking import o_primeiro_do_ranking

from tests.entradas_e_saidas import es_o_primeiro_do_ranking, testes_de_erro


class TestOPrimeiroDoRanking(unittest.TestCase):

    def test_deve_lancar_erro_em_caso_de_valores_invalidos(self):
        for i in range(len(testes_de_erro.DADOS)):
            teste = testes_de_erro.DADOS[i]['teste']
            with self.subTest(msg=teste, i=i):
                qtd_pontuacoes = testes_de_erro.DADOS[i]['qtd_pontuacoes']
                pontuacoes = testes_de_erro.DADOS[i]['pontuacoes']
                qtd_pontuacoes_do_joaozinho = testes_de_erro.DADOS[i]['qtd_pontuacoes_do_joaozinho']
                pontuacoes_do_joaozinho = testes_de_erro.DADOS[i]['pontuacoes_do_joaozinho']

                with self.assertRaises(ValueError):
                    o_primeiro_do_ranking(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho)

    def test_deve_retornar_posicoes_quando_classificacao_e_pequena(self):
        qtd_pontuacoes = 7
        pontuacoes = [100, 100, 50, 40, 40, 20, 10]
        qtd_pontuacoes_do_joaozinho = 4
        pontuacoes_do_joaozinho = [5, 25, 50, 120]

        resposta = o_primeiro_do_ranking(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho)

        self.assertEqual([6, 4, 2, 1], resposta)

    def test_deve_retornar_posicoes_quando_classificacao_e_um_pouco_maior(self):
        qtd_pontuacoes = es_o_primeiro_do_ranking.ENTRADA_TESTE_1['qtd_pontuacoes']
        pontuacoes = list(map(int,es_o_primeiro_do_ranking.ENTRADA_TESTE_1['pontuacoes'].rstrip().split()))
        qtd_pontuacoes_do_joaozinho = es_o_primeiro_do_ranking.ENTRADA_TESTE_1['qtd_pontuacoes_joaozinho']
        pontuacoes_do_joaozinho = list(map(int, es_o_primeiro_do_ranking.ENTRADA_TESTE_1['pontuacoes_joaozinho'].rstrip().split()))

        resposta = o_primeiro_do_ranking(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho)

        resposta_esperada = list(map(int, es_o_primeiro_do_ranking.SAIDA_TESTE_1.rstrip().split()))
        self.assertEqual(resposta_esperada, resposta)

    def test_deve_retornar_posicoes_rapidamente_quando_classificacao_e_colossal(self):
        qtd_pontuacoes = es_o_primeiro_do_ranking.ENTRADA_TESTE_3['qtd_pontuacoes']
        pontuacoes = list(map(int,es_o_primeiro_do_ranking.ENTRADA_TESTE_3['pontuacoes'].rstrip().split()))
        qtd_pontuacoes_do_joaozinho = es_o_primeiro_do_ranking.ENTRADA_TESTE_3['qtd_pontuacoes_joaozinho']
        pontuacoes_do_joaozinho = list(map(int, es_o_primeiro_do_ranking.ENTRADA_TESTE_3['pontuacoes_joaozinho'].rstrip().split()))

        tempo_de_inicio = time.time()
        resposta = o_primeiro_do_ranking(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho)
        tempo_de_execucao = time.time() - tempo_de_inicio

        resposta_esperada = list(map(int, es_o_primeiro_do_ranking.SAIDA_TESTE_3.rstrip().split()))
        self.assertEqual(resposta_esperada, resposta)
        self.assertTrue(tempo_de_execucao < 5) # Caso não consiga fazer em menos de 5 segundos, tente chegar o mais proximo disso
