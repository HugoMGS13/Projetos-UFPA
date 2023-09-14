def calcular_saldo_médio(cadastros):
    saldo_médio = 0
    for elemento in cadastros:
        saldo_médio += saldo_médio + elemento["saldo"]
    return saldo_médio / len(cadastros)

#filtro de lista dinamica
def filtrar_por_emaiLl(cadastros,tipodemail):
    lista_filtrada = []
    for elemento in cadastros.copy():
        if tipodemail not in elemento["email"]:
            lista_filtrada.append(elemento)
    return lista_filtrada()

#filtra a lista por saldo
def filtrar_por_saldo(cadastros, saldo, parametro):
    lista_filtrada = []
    for elemento in cadastros.copy():
        if parametro.upper == "maior" and elemento["saldo"]  > saldo:
            lista_filtrada.append(elemento)
    # for elemento in cadastros:
    #     if elemento >= 1000 in elemento["saldo"]:
    # return lista_por_saldo 

#dois dicionarios dentro de uma lista
cadastrosos = [{"nome":"mingau","email":"mingau@gmail.com","saldo":58},{"nome":"roger","email":"roger@gmail.com","saldo":10.24}]

def extrair_nomes(cadastrosos):
    lista_com_nomes = []
    for nomes in cadastrosos:
        lista_com_nomes.append(nomes["nome"])
    return lista_com_nomes

def formatar_nomes(lista,tipo):
    """
    Mapeia uma lista de string para uma lista de string em caixa alta
    Argumentos:
        lista: lista de string
        tipo: objetivo de função
    Retorno:
        lista de string em caixa alta
    """
    lista_caixaalta=[]
    for item in lista:
        if tipo == 'CAIXA_ALTA':
            lista_caixaalta.append(item.upper())
        elif tipo == 'CAIXA_BAIXA':
            lista_caixaalta.append(item.lower())
        else:
            continue
    if len(lista_caixaalta) == 0:
        lista_caixaalta.append('Segundo parametro inexistente')
    return lista_caixaalta[0]

def filtrar_por_tipo(lista,tipo):
    lista_filtrada = []
    for item in lista:
        if type(item) == tipo:
            lista_filtrada.append(item)
    return lista_filtrada

def tamanho_dos_nomes(lista):
    lista_numeros = []
    for item in lista:
        lista_numeros.append(len(item))
    return lista_numeros
