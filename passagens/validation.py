def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e Destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se o campo tem algum número"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números neste campo'

def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """Verica se data de ida é maior que a data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'A data de ida não pode ser menor que a data de volta'

def data_ida_menor_data_de_hoje(data_ida, data_pesquisa, lista_de_erros):
    """Verica se data de ida não é menor que a data de hoje"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_pesquisa'] = 'A data de Ida não pode ser menor que a data de hoje'