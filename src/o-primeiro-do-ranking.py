'''
Joãozinho está jogando fliperama e quer ser o primeiro no top dos melhores e acompanhar o seu progresso. O jogo usa o modelo de classificação densa, onde o jogador com a maior pontuação recebe a posição 1, e assim por diante. Jogadores que tiverem a mesma pontuação, recebem a mesma posição.
Por exemplo, para os 4 melhores jogadores com pontuação 100, 90, 90 e 80, as posições na classificação serão 1, 2, 2 e 3 respectivamente.
Se o joãozinho pontua 70, 80 e 105, sua classificaçao a cada rodada são 4º, 3º e 1º.

Descrição da Função

Complete a função x abaixo. Ela deve retornar uma lista de inteiro onde cada elemento res[j] representa uma posição da classificação depois da rodada j.
A função possui os seguintes parametros:
* pontuacoes: uma lista de inteiros que representa as pontuacoes da classificação
* pontuacoes_do_joaozinho: Uma lista de inteiros que representa as pontuações do joãozinho.


Formato de entrada

A primeira linha tem um inteiro n, o número de jogadores na classificação.
A próxima linha tem n numeros separados por espaços (pontuacoes[i], as pontuações da classificação em ordem decrescente.
A próxima linha tem um inteiro m, a quantidade de rodadas que o Joãozinho jogou.
A última linha tem m inteiros separados por espaço (pontuacoes_do_joaozinho[j]), as pontuagoes da rodada.

Restrições
1 <= n <= 2 x 10^5
1 <= m <= 2 x 10^5
0 <= pontuacoes[i] <= 10^9 para 0 <= i < n
0 <= pontuacoes_do_joaozinho[i] <= 10^9 para 0 <= j < m
A classificação atual, pontuacoes, está em ordem decrescente.
As pontuações do joãozinho, estão em ordem crescente.

Sub-tarefa

para 60% da pontuação máxima
1 <= n <= 200
1 <= m <= 200

Formato de saída

Imprima m inteiros. O inteiro j deve indicar a posição de Joãozinho depois de ter jogado a rodada j.


Amostra de input

7
100 100 50 40 40 20 10
4
5 25 50 120

_______________________________
|100 |100 | 50| 40| 40| 20| 10|
-------------------------------
Lista: pontuacoes
_________________
|5 |25 | 50| 120|
-----------------
Lista: pontuacoes_do_joaozinho


Amostra de Output

6
4
2
1


Explicação

Joãozinho começa jogando com 7 jogadores na classificação, como na tabela abaixo:


_______________________________
| Posição |    Nome    | Nota |
-------------------------------
| 1      | Geraldo     | 100  |
| 1      | Geilson     | 100  |
| 2      | Adagalmir   | 50   |
| 3      | Valmira     | 40   |
| 3      | Cleberson   | 40   |
| 4      | Shirley     | 20   |
| 5      | Carolaine   | 10   |
-------------------------------

Depois que o joãozinho terminou a rodada 0, sua pontuação é 5 e seu lugar na classificação é 6.

_______________________________
| Posição |    Nome    | Nota |
-------------------------------
| 1      | Geraldo     | 100  |
| 1      | Geilson     | 100  |
| 2      | Adagalmir   | 50   |
| 3      | Valmira     | 40   |
| 3      | Cleberson   | 40   |
| 4      | Shirley     | 20   |
| 5      | Carolaine   | 10   |
| 6      | Joãozinho   | 5    |
-------------------------------


'''