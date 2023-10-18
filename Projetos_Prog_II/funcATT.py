from math import sqrt

def numeroprimo(num):
  """
  Função pra saber se o número é um número primo
  """
  for conta in range(2,num):
    if num % conta == 0:
      return False
    else:
      continue
  return True

def encontrar_primo(num):
  num+=1
  while True:
    if numeroprimo(num) == True:
      return num
    else:
      num+=1
    
def q1(lista1,lista2):
  """
  Dada duas listas de string de mesmo tamanho, faça o mapeamento para obter uma lista em que cada elemento seja a concatenação dos elementos de mesmo índice das duas listas. 
  """
  lista_nova = []
  índice = 0
  for elemento_lista1 in lista1:
    lista_nova.append(elemento_lista1+lista2[índice])
    índice += 1
  return lista_nova

def q1_compressed(lista1,lista2):
   return [(a+b) for a,b in zip(lista1,lista2)]

def q2(lista):
   lista_nova = []
   for item in lista:
      lista_nova.append(encontrar_primo(item))
   return lista_nova
      
def q2_compressed(lista):
    return[encontrar_primo(item) for item in lista]

def q3(lista):
  """
  Dada uma lista de string, faça um filtro para obter uma lista somente com os elementos cujo tamanho da string seja menor que 10. A lista resultante deve estar ordenada em ordem alfabética.
  """
  lista_nova = []
  for elemento in lista:
    if len(elemento) < 10:
      lista_nova.append(elemento)
  return sorted(lista_nova)

def q3_compressed(lista):
   return sorted([elemento for elemento in lista if len(elemento) < 10])

#falta fazer: def q4()

def q5(listaint,listastr):
  """
  Dada uma lista de string e uma lista de números inteiros, faça um filtro para obter uma lista de string onde o tamanho do elemento é menor ou igual ao valor do número inteiro de índice correspondente
  """
  lista_nova = []
  indice = 0
  for elemento in listastr:
    if len(elemento) <= listaint[indice]:
      lista_nova.append(elemento)
      indice += 1
    else:
      indice += 1
  return lista_nova

def q6(listao):
  """
  Dada uma lista onde cada elemento corresponde a uma lista de números
  inteiros, faça um filtro para obter uma lista de listas onde a soma dos elementos da
  lista de uma determinada posição é maior que a soma dos elementos da lista da
  próxima posição. 
  """
  lista_nova = []
  for listinha in listao:
    if sum(listinha) <= listao.index(listinha)+1:
      lista_nova.insert(listao.index(listinha),listinha)
    else:
      lista_nova.append(listinha)
  return lista_nova
    
def q7(lista1,lista2,lista3):
  """
  Dada três lista de números inteiros, faça uma redução para encontrar o
  menor número resultante da soma dos elementos de índices correspondentes.
  """
  indice = 0
  result = lista1[0]+lista2[0]+lista3[0]
  for elemento in lista1:
    soma = elemento + lista2[indice] + lista3[indice]
    indice += 1
    if soma <= result:
      result = soma
    elif soma > result:
      continue
  return result

##def q8(lista):
#  """
 #   Dada uma lista de string, faça uma redução para determinar o tamanho da
  #  maior string. Retorne o valor encontrado e o índice correspondente na lista. Se mais de
   # uma string possuir o maior tamanho, retorne o menor índice.
    #"""
    #medidor = len(lista[0])
    #for string in lista:
      #  if len(string) >= medidor:
       #     medidor = len(string)
       
#def q9(lista):
  #  """
 #   Dada uma lista de números reais, faça uma redução que implique na soma
   # dos elementos. O elemento da posição i só pode ser somado se ele for maior que o
   # elemento da posição i+1 (INCOMPLETA)
   # """
   # veri = 0
   # indice = lista[1]
   # for elemento in lista:
    #    if elemento > lista[elemento+1]:
     #       indice += 1
      #      veri += 1
    #if veri == len(lista):
     #   return sum(lista)
    #else:
     #   return 'Essa lista não está ordenada em ordem decrescente'
     
def q10(lista):
  """
  Dada uma lista de string, faça uma redução que resulte em uma string
  concatenando todos os elementos separados por vírgula e espaço em branco.
  """
  conc = ''
  for elemento in lista:
    conc += elemento
  elementonovo = conc.replace(" ","")
  elementonovo = elementonovo.replace(",","")
  return elementonovo
  
def q11(lista):
  """
  Dada uma lista de números inteiros, faça uma redução para retornar o
  índice do maior primo da lista. Caso não exista, retorne -1.
  """
  listadecompa = []
  compa = 0
  for elemento in lista:
    if numeroprimo(elemento) == True and elemento > compa:
      listadecompa.append(elemento)
      indice = lista.index(elemento)
      if elemento not in listadecompa:
        compa += elemento
    else:
      continue
  if len(listadecompa) == 0:
    return -1
  else:
    return indice

def q12(lista):
  """
  Dada uma lista de números reais, faça uma redução para calcular o desvio
  padrão. Retorne o valor encontrado
  """
  media = sum(lista) / len(lista)
  somatorio = 0
  for elemento in lista:
    somatorio += (elemento-media)**2
  return sqrt(somatorio/len(lista))

def q13(lista,num):
  """
  Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
  função que faça uma busca linear do elemento e retorne quantas comparações foram
  necessárias, bem como true ou false para informar se a busca foi realizada com sucesso
  ou não.
  """
  comp = 0
  for elemento in lista:
    if elemento == num:
      comp += 1
      return comp, True
    else:
      comp += 1
  if num not in lista:
    return False

def q14(lista,num):
  """
  Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
  função que ordene a lista e faça uma busca linear do elemento e retorne quantas
  comparações foram necessárias, bem como true ou false para informar se a busca foi
  realizada com sucesso ou não
  """
  comp = 0
  lista.sort()
  for elemento in lista:
    if elemento == num:
      comp += 1
      return comp, True
    else:
      comp += 1
  if num not in lista:
    return False
  
def q15(lista):
  """
  Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
  função que ordene a lista e faça uma busca binária do elemento e retorne quantas
  comparações foram necessárias, bem como true ou false para informar se a busca foi
  realizada com sucesso ou não. (INCOMPLETA(ESTUDAR BUSCA BINÁRIA))
  """

def q16(lista,valor):
  """
  Crie uma função para receber uma lista e um valor de referência, retorne
  a frequência deste valor na lista.
  """
  freq = 0
  for elemento in lista:
    if elemento == valor:
      freq += 1
  return freq

def q17(lista):
  """
  Crie uma função para receber uma lista de números inteiros e retorne
  uma lista de dicionário. Para cada dicionário, a chave deve ser um valor da lista e o
  valor deve ser a sua frequência.
  """
  dict = {}
  for elemento in lista:
    freq = q16(lista,elemento)
    dict[elemento]=freq
  return dict

def q1SBC(lista):
    qntd_errada = 0
    for embalagem in lista:
       if embalagem < 7:
          qntd_errada += 1
    return qntd_errada
  
def q2sbc(lista,media):
  result = 0
  for nota in lista:
    if nota > media:
      result += 1
    else:
      continue
  return result

def q2sbc_compressed(lista,media):
  return sum([1 for nota in lista if nota > media])
      
def q3sbc(lista):
  return max(lista)

def q4sbc(lista):
  lista_nova = []
  for num in lista:
    if num % 2 == 0:
      lista_nova.append(num)
    else:
      continue
  return (sum(lista_nova)//len(lista_nova))

#def q4sbc_compressed(lista):
  return[sum(num) for num in lista if num % 2 == 0]//sum(num)

def q5sbc(lista,alvo):
  repetição = 0
  for elemento in lista:
    if elemento == alvo:
      repetição += 1
    else:
      continue
  return repetição

def q5sbc_compressed(lista,alvo):
  return sum([1 for elemento in lista if elemento == alvo])
