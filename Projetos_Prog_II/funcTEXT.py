def ler_txt(arquivo):
    with open(arquivo,'r', encoding='UTF-8') as file:
        texto = file.read()
        print(texto)

def escrever_txt(arquivo):
    with open(arquivo, "w") as file:
        arq = file.write('Sou viado')

def editar_txt(arquivo, texto):
    with open(arquivo, 'a') as file:
        file.write(texto)

def menu():
    while True:
        op = input('Digite o que quer fazer:\n1 - Cadastrar\n2 - Listar\n* - Sair\n')
        if op == 1:
            cadastrar()
        else:
            break

def cadastrar():
    nome = input('Nome: ')
    tel = input('Telefone: ')
    email = input('Email: ')
