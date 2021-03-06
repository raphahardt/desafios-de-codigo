DADOS = [
    {
        'teste': 'qtd_pontuacoes menor que 0.',
        'error_message': 'qtd_pontuacoes inválido. Deve ser entre 1 e 200000',
        'qtd_pontuacoes': 0,
        'pontuacoes': [],
        'qtd_pontuacoes_do_joaozinho': 1,
        'pontuacoes_do_joaozinho': [1],
    },
    {
        'teste': 'qtd_pontuacoes maior que 200000.',
        'error_message': 'qtd_pontuacoes inválido. Deve ser entre 1 e 200000',
        'qtd_pontuacoes': 9999999999,
        'pontuacoes': [],
        'qtd_pontuacoes_do_joaozinho': 1,
        'pontuacoes_do_joaozinho': [1],
    },
    {
        'teste': 'qtd_pontuacoes_do_joaozinho menor que 0.',
        'error_message': 'qtd_pontuacoes_do_joaozinho inválido. Deve ser entre 1 e 200000',
        'qtd_pontuacoes': 1,
        'pontuacoes': [1],
        'qtd_pontuacoes_do_joaozinho': 0,
        'pontuacoes_do_joaozinho': [],
    },
    {
        'teste': 'qtd_pontuacoes_do_joaozinho maior que 200000.',
        'error_message': 'qtd_pontuacoes_do_joaozinho inválido. Deve ser entre 1 e 200000',
        'qtd_pontuacoes': 1,
        'pontuacoes': [1],
        'qtd_pontuacoes_do_joaozinho': 9999999999,
        'pontuacoes_do_joaozinho': [],
    },
    {
        'teste': 'Valor de pontuacoes maior que 1000000000.',
        'error_message': 'pontuacoes inválido. Os valores da lista devem ser entre 0 e 1000000000',
        'qtd_pontuacoes': 2,
        'pontuacoes': [999999999999, 999999999999],
        'qtd_pontuacoes_do_joaozinho': 1,
        'pontuacoes_do_joaozinho': [1],
    },
    {
        'teste': 'Valor de pontuacoes menor que 0.',
        'error_message': 'pontuacoes inválido. Os valores da lista devem ser entre 0 e 1000000000',
        'qtd_pontuacoes': 2,
        'pontuacoes': [-1, -1],
        'qtd_pontuacoes_do_joaozinho': 1,
        'pontuacoes_do_joaozinho': [1],
    },
    {
        'teste': 'Valor de pontuacoes_do_joaozinho maior que 1000000000.',
        'error_message': 'pontuacoes_do_joaozinho inválido. Os valores da lista devem ser entre 0 e 1000000000',
        'qtd_pontuacoes': 1,
        'pontuacoes': [1],
        'qtd_pontuacoes_do_joaozinho': 2,
        'pontuacoes_do_joaozinho': [999999999999, 999999999999],
    },
    {
        'teste': 'Valor de pontuacoes_do_joaozinho menor que 0.',
        'error_message': 'pontuacoes_do_joaozinho inválido. Os valores da lista devem ser entre 0 e 1000000000',
        'qtd_pontuacoes': 1,
        'pontuacoes': [1],
        'qtd_pontuacoes_do_joaozinho': 2,
        'pontuacoes_do_joaozinho': [-1, -1],
    },
    {
        'teste': 'qtd_pontuacoes diferente do tamanho da lista pontuacoes.',
        'error_message': 'qtd_pontuacoes deve ter o valor do tamanho da lista pontuacoes',
        'qtd_pontuacoes': 5,
        'pontuacoes': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        'qtd_pontuacoes_do_joaozinho': 1,
        'pontuacoes_do_joaozinho': [1],
    },
    {
        'teste': 'qtd_pontuacoes_do_joaozinho diferente do tamanho da lista pontuacoes_do_joaozinho.',
        'error_message': 'qtd_pontuacoes_do_joaozinho deve ter o valor do tamanho da lista pontuacoes_do_joaozinho',
        'qtd_pontuacoes': 1,
        'pontuacoes': [1],
        'qtd_pontuacoes_do_joaozinho': 5,
        'pontuacoes_do_joaozinho': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
]
