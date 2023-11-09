import re
def val_cpf(cpf):
    #cpf = CPF a ser checado
    check = r'\d{3}\.\d{3}\.\d{3}-\d{2}' #Modelo certo de CPF escrito em expressão
    func = re.fullmatch(check, cpf) #Checagem da string em relação a expressão usando a função search
    if check: #Se der fullmatch com check
        print('Ok')
    else: #Se não
        print('Inválido')
    print(func)
    #resultado= <re.Match object; span=(0, 14), match='192.168.100-33'>
    # Retornou um objeto match; dentro dos índices de substring 0 e 14; com a seguinte string 
def val_num(num):
    check1 = r'\(\d{2}\)\s9\d{4}-\d{4}'
    func1 = re.fullmatch(check1, num)
    if check1:
        telefone = re.sub('[\(\)\-\s]','',num)
        print('Ok')
        print(telefone)
    else:
        print('Inválido')
    print(func1)

def val_rg(uf):
    regex = r'[A-Z]{2}'
    check = re.fullmatch(regex,uf)
    if check:
        print('UF ok')
    else:
        print('UF inválido')

def ex_1RE(string):
    regex = r'A{2,}'
    check = re.fullmatch(regex, string)
    if check and len(string) % 2 == 0:
        print('Ok')
    else:
        print('No')

def main():
    while True:
        senha = input('Digite uma senha forte: ')
        if muito_forte(senha):
            print('Senha muito forte')
        elif forte(senha):
            print('Senha forte')
            break
        elif media(senha):
            print('Senha media')
        elif fraca(senha):
            print('Senha fraca')

def muito_forte(senha): 
    return re.search("[A-Z]", senha) and\
         re.search('[a-z]', senha) and\
         re.search('[0-9]', senha) and\
         len(re.findall("[A-Za-z0-9]", senha)) >= 3 and\
         len(senha) >= 10 #Se nenhuma dessas der certo, retorna False, se todas derem certo, retorna True

def forte(senha):
    return re.search('[A-Z]', senha) and\
    re.search('[a-z]', senha) and\
    re.search('\d',senha) and\
    re.search('\W',senha) and\
    len(senha) >= 8

def media(senha):
    return re.search('[A-Z]',senha) and\
    re.search('[a-z]',senha) and\
    re.search('\d', senha) and\
    len(senha) >= 6

def fraca(senha):
    return len(senha) >= 6

main()

