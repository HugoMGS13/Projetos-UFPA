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

import re
import datetime

def main():
    while True:
        op = menu()
        if op == '1':
            cadastrar()
        elif op == '2':
            listar()
        else:
            break

def menu():
    return input('1 - cadastrar \n2 - listar \n*- Sair \n')

def cadastrar():
    while True:
        try:
            regex_nome = re.compile(r'[A-Za-zÁ-Úá-ú]{3,}')
            regex_telefone = re.compile(r'\d{2}\s\d{9}')
            regex_email = re.compile(r'\w{4,}@\w{5,}\.com')
            nome = input("Digite seu nome: ")
            telefone = input("Digite seu telefone: ")
            email = input("Digite seu email: ")
            check1 = regex_nome.fullmatch(nome)
            check2 = regex_telefone.fullmatch(telefone)
            check3 = regex_email.fullmatch(email)
            if check1 and check2 and check3:
                with open('bd_cadastros.txt', 'a', encoding= 'utf-8') as f:
                    f.write(f'CADASTRO de {datetime.date.today()}: Nome: {nome}, Email: {email}, Telefone: {telefone}')
                    f.write('\n')
                    break
        except Exception as e:
            print(e,'- ERRO. Repita o procedimento.')
        else:
            print('ERRO. Repita o procedimento.')

def listar():
    with open("bd_cadastros.txt", 'r', encoding="utf-8") as f:
        lista = [linha for linha in f]
    print(*lista) #O asterísco antes da variável de coleção indica que eu só quero printar os itens da lista, e não a estrutura

#def formatar(linha):
#   return re.sub(r'\s*,\s*', ', ', linha)

main()
