def load_data_base(): #cada item da primeira linha do arquivo vai virar uma chave do dicionário do banco de dados no código
    with open('datatran2020.csv', 'r', encoding='utf-8') as f:
        dados = [linha.split(',') for linha in f] #Vai criar uma lista com cada item separado por vírgula nas linhas do arquivo (onde cada lista dentro da lista é uma linha do arquivo)
        colunas = dados[0]
        bd = dict()
        for id, coluna in enumerate(colunas): #enumerate vai percorrer uma lista e vai retornar seus índice do item e o próprio item
            bd[coluna] = [item[id] for item in dados[1:]]
    return bd

def questao_02():
    bd = load_data_base()
    valores = bd['fase_dia']
    colunas = set(valores)
    freq_fase_dia = dict()
    for coluna in colunas:
        freq_fase_dia[coluna] = sum([1 for item in valores if item == coluna])
    print(freq_fase_dia)

def questao_04():
    bd = load_data_base()
    ufs = bd['uf']
    mortes = bd['mortos']
    total = sum([int(valor) for uf, valor in zip(ufs,mortes) if uf == 'PA'])
    print(total)

questao_04()
