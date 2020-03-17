
class Ranking(object):
    def __init__(self, pontuacoes, qtd_pontuacoes):
        self.__pontuacoes = pontuacoes
        self.__qtd_pontuacoes = qtd_pontuacoes
        self.__rank = None
        self.__last_index = 0
        self.__found_first_rank = False

        # adiciono uma pontuação "bogus" de "último lugar" nas pontuações
        # para assim, a lógica de comparação eu não precise fazer nenhum desvio técnico
        self.__pontuacoes.append(0)
        self.__qtd_pontuacoes += 1

    def get_rank_from_pontuacao(self, pontuacao):
        """
        Retorna o rank dado uma pontuação de uma rodada.
        """
        if not self.__found_first_rank:
            iterator = self.__iterate_to_find_first_rank
        else:
            iterator = self.__iterate_to_find_subsequent_ranks

        for rank, i in iterator():
            if self.__is_rank_pontuacao(pontuacao, i):
                # se o rank dessa rodada for encontrado
                # coloco ele no ranking
                # PS: eu não faço "shift" dos outros colocados no ranking
                # porque o teste não pediu, então não é necessário
                self.__pontuacoes[i] = pontuacao

                # marco que encontrei o primeiro rank se eu ainda não tiver encontrado
                if not self.__found_first_rank:
                    self.__found_first_rank = True

                # e interrompo a iteracao
                return rank

    def __is_rank_pontuacao(self, pontuacao, i):
        """
        Retorna True se uma pontuação fazer parte do ranking, dado um index i
        da posição do ranking
        Uso interno da classe, e funciona junto dos métodos '__iterate_to_find_first_rank'
        e '__iterate_to_find_subsequent_ranks'
        """
        # se está procurando o primeiro rank
        if not self.__found_first_rank:
            # se está no último indice do ranking, então com certeza é o rank
            # (lembrando que o ranking tem uma pontuação "bogus" de zero pra justamente
            # ter um último lugar pra comparar)
            if i == self.__qtd_pontuacoes:
                return True

            # caso contrario, a pontuação da rodada só é do ranking se ela for igual ou maior que a
            # pontuação do ranking iterada
            return pontuacao >= self.__pontuacoes[i]

        # se está procurando os ranks subsequentes
        else:
            # se chegou no "fim" do ranking (que no caso seria o começo), significa que
            # é primeiro lugar no ranking, então sempre retornar true
            if i == 0:
                return True

            # caso contrario, a pontuação da rodada só é do ranking se ela for igual ou maior que a
            # pontuação do ranking iterada e menor que a pontuação do rank anterior
            return self.__pontuacoes[i] <= pontuacao < self.__pontuacoes[i - 1]

    def __iterate_to_find_first_rank(self):
        """
        Generator que percorre cada pontuação no ranking e envia pro
        iterador:
        - o rank daqueles pontos
        - o indice daqueles pontos na lista de pontuação

        O generator vai correr em ordem crescente. Ele é usado apenas pra encontrar
        o primeiro rank possível de uma pontuação. Ao encontrar, ele lembra onde parou
        para que o segundo generator continue correndo, mas de forma decrescente
        """
        self.__rank = 0
        prox_pontuacao = None

        for i in range(self.__qtd_pontuacoes):
            if self.__pontuacoes[i] != prox_pontuacao:
                self.__rank += 1
                prox_pontuacao = self.__pontuacoes[i]

            self.__last_index = i
            yield self.__rank, i

    def __iterate_to_find_subsequent_ranks(self):
        """
        Generator que percorre cada pontuação no ranking e envia pro iterador:
        - o rank daqueles pontos
        - o indice daqueles pontos na lista de pontuação

        O generator vai correr na ordem inversa, a partir do ponto onde o primeiro generator
        parou. As próximas chamadas dele ele sempre vai continuar de onde parou também.
        """
        i = self.__last_index
        prox_pontuacao = self.__pontuacoes[i]
        yield self.__rank, i

        while 0 <= i:
            i -= 1
            if self.__pontuacoes[i] != prox_pontuacao:
                self.__rank -= 1
                prox_pontuacao = self.__pontuacoes[i]

            self.__last_index = i
            yield self.__rank, i
