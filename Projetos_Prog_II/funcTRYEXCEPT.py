def validar_ano_de_nascimento(arg):
    try:
        if not arg.isdigit():
            raise Exception('Nascimento inválido')
        if 1900 > int(arg) > 2023:
            raise Exception('Nascimento inválido')
    except Exception as e:
        print(e)
    else:
        return True

def validar_cpf(arg):
    try:
        if not arg.isdigit():
            raise Exception('CPF inválido')
        if len(arg) != 11:
            raise Exception('CPF inválido')
    except Exception as e:
        print(e)
    else:
        return True
        
def validar_rg(arg):
    try:
        if not arg.isdigit():
            raise Exception('RG inválido')
        if len(arg) != 9:
            raise Exception('RG inválido')
    except Exception as e:
        print(e)
    else:
        return True

def validar_telefone(arg):
    try:
        if not arg.isdigit():
            raise Exception('Telefone inválido')
        if len(arg) != 9:
            raise Exception('Telefone inválido')
        if arg[0] != '9':
            raise Exception('Telefone inválido. O 9 não está no primeiro dígito')
    except Exception as e:
        print(e)
    else:
        return True

def validar_uf(arg):
    try:
        if not arg.isalpha():
            raise Exception('UF inválido')
        if len(arg) != 2:
            raise Exception('UF inválido')
    except Exception as e:
        print(e)
    else:
        return True

def main():
    nasc = input('Digite seu ano de nascimento:\n')
    cpf = input('Digite seu cpf:\n')
    rg = input('Digite seu RG:\n')
    tel = input('Digite seu telefone:\n')
    uf = input('Digite sua Unidade Federativa:\n')
    
    validar_ano_de_nascimento(nasc)
    validar_cpf(cpf)
    validar_rg(rg)
    validar_telefone(tel)
    validar_uf(uf)
    
    if validar_ano_de_nascimento(nasc) == True and validar_cpf(cpf) == True and validar_rg(rg) == True and validar_telefone(tel) == True and validar_uf(uf) == True:
        print('Cadastro realizado com sucesso')
    
main()
    