
def validar_parametros(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho):
    if qtd_pontuacoes < 1 or qtd_pontuacoes > 200000:
        raise ValidacaoError('qtd_pontuacoes inválido. Deve ser entre 1 e 200000')

    if qtd_pontuacoes_do_joaozinho < 1 or qtd_pontuacoes_do_joaozinho > 200000:
        raise ValidacaoError('qtd_pontuacoes_do_joaozinho inválido. Deve ser entre 1 e 200000')

    # como as pontuacoes vem sempre em ordem decrescente, só preciso ver se o primeiro
    # elemento é maior do que a pontuação máxima
    if pontuacoes[0] > 10000000000 or pontuacoes[-1] < 0:
        raise ValidacaoError('pontuacoes inválido. Os valores da lista devem ser entre 0 e 1000000000')

    # no caso dos pontos do joaozinho, é o contrario, pois os pontos vem sempre em ordem crescente
    if pontuacoes_do_joaozinho[-1] > 10000000000 or pontuacoes_do_joaozinho[0] < 0:
        raise ValidacaoError('pontuacoes_do_joaozinho inválido. Os valores da lista devem ser entre 0 e 1000000000')

    if qtd_pontuacoes != len(pontuacoes):
        raise ValidacaoError('qtd_pontuacoes deve ter o valor do tamanho da lista pontuacoes')

    if qtd_pontuacoes_do_joaozinho != len(pontuacoes_do_joaozinho):
        raise ValidacaoError('qtd_pontuacoes_do_joaozinho deve ter o valor do tamanho da lista pontuacoes_do_joaozinho')


class ValidacaoError(Exception):
    def __init__(self, message):
        self.message = message
