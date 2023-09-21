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

# falta fazer: def q2()

def q3(lista):
  """
  Dada uma lista de string, faça um filtro para obter uma lista somente com os elementos cujo tamanho da string seja menor que 10. A lista resultante deve estar ordenada em ordem alfabética.
  """
  lista_nova = []
  for elemento in lista:
    if len(elemento) < 10:
      lista_nova.append(elemento)
  return sorted(lista_nova)

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

# def q6(lista):
#    """
 #   Dada uma lista onde cada elemento corresponde a uma lista de números
  #  inteiros, faça um filtro para obter uma lista de listas onde a soma dos elementos da
   # lista de uma determinada posição é maior que a soma dos elementos da lista da
    #próxima posição. 
    #"""
    
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
