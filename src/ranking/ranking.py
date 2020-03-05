
class Ranking:
    __pontuacoes = []
    __qtd_pontuacoes = 0

    # iniciais
    __rank = 1
    __last_index = 0
    __iteracao_direcao = 1

    def __init__(self, pontuacoes, qtd_pontuacoes):
        self.__pontuacoes = pontuacoes
        self.__qtd_pontuacoes = qtd_pontuacoes

        # adiciono uma pontuação "bogus" de "último lugar" nas pontuações
        # para assim, a lógica de comparação eu não precise fazer nenhum desvio técnico
        # como eu estava fazendo antes na primeira versão
        self.__pontuacoes.append(0)
        self.__qtd_pontuacoes += 1

    def get_rank_joaozinho(self, pontos_joaozinho):
        """
        Retorna o rank do joaozinho, dado os pontos dele em uma rodada.
        """
        for [rank, i] in self.__iterar_em_pontuacoes():
            if self.__is_rank_joaozinho(pontos_joaozinho, i):
                # se o rank do joaozinho for encontrado
                # coloco ele no ranking
                # PS: eu não faço "shift" dos outros colocados no ranking
                # porque o teste não pediu, então não é necessário
                self.__pontuacoes[i] = pontos_joaozinho

                # pra performance, após a iteração sobre o ranking correr de forma crescente,
                # eu inverto a ordem pra correr a partir do último indice antes do return
                if self.__iteracao_direcao == 1:
                    self.__iteracao_direcao = -1

                # e interrompo a iteracao
                return rank

    def __is_rank_joaozinho(self, pontos_joaozinho, i):
        """
        Retorna True se uma pontuação do joaozinho fazer parte do ranking, dado um index i
        da posição do ranking
        """
        if self.__iteracao_direcao == 1:
            retorno = i == self.__qtd_pontuacoes or pontos_joaozinho >= self.__pontuacoes[i]
        else:
            retorno = i == 0 or (self.__pontuacoes[i] <= pontos_joaozinho < self.__pontuacoes[i - 1])

        return retorno

    def __iterar_em_pontuacoes(self):
        """
        Generator que percorre cada pontuação no ranking e envia pro iterador:
        - o rank daqueles pontos
        - o indice daqueles pontos na lista de pontuação

        O generator vai correr na ordem crescente ou decrescente conforme a
        propriedade iteracao_direcao. O generator vai continuar sempre de onde
        parou
        """
        i = self.__last_index
        prox_pontuacao = self.__pontuacoes[i]
        yield [self.__rank, i]

        while 0 <= i <= self.__qtd_pontuacoes - 1:
            i += 1 * self.__iteracao_direcao
            if self.__pontuacoes[i] != prox_pontuacao:
                self.__rank += 1 * self.__iteracao_direcao
                prox_pontuacao = self.__pontuacoes[i]

            self.__last_index = i
            yield [self.__rank, i]
