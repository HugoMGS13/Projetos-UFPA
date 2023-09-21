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