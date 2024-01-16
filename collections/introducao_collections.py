
# idades = [20, 39, 18, 27, 19]
# print(idades)

# print(idades[0])

# idades.append(15)
# print(idades)

# print(len(idades))
# print(type(idades))

# for idade in idades:
#   print(idade)

# idades_ano_que_vem = []
# for idade in idades:
#   idades_ano_que_vem.append(idade+1)
# print(idades_ano_que_vem)

# novas_idades = [(idade+1) for idade in idades]
# print(novas_idades)

# print([idade for idade in idades if idade > 21])

# def proximoAno(idade):
#   return idade + 1

# print([proximoAno(idade) for idade in idades if idade > 21])

# def faz_processamento_de_visualizacao(lista = None):
#    if lista == None:
#     lista = list()
#    print(len(lista))
#    print(lista)
#    lista.append(13)

# idades = [16,21,29,56,43]
#   faz_processamento_de_visualizacao()
#   faz_processamento_de_visualizacao()
#   faz_processamento_de_visualizacao()
#   faz_processamento_de_visualizacao()

#   print(idades)

def teste1():
  idades = [15, 87, 32, 65, 56, 32, 49, 37]
  for i in range(len(idades)):
    print("idades[{}] = {}".format(i, idades[i]))

def teste2():
  idades = [15, 87, 32, 65, 56, 32, 49, 37]
  list(range(len(idades)))

def teste3():
  idades = [15, 87, 32, 65, 56, 32, 49, 37]
  print(list(enumerate(idades)))

def teste4():
  idades = [15, 87, 32, 65, 56, 32, 49, 37]
  for indice, valor in enumerate(idades):
    print(indice, valor)

def teste5():
  usuarios = [
    ("Gulherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
  ]
  for nome, idade, nascimento in usuarios:
    print(nome)

def teste6():
  usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
  ]
  for nome, _, _ in usuarios:
    print(nome)

def teste7():
  idades = [15, 87, 32, 65, 56, 32, 49, 37]
  print(sorted(idades))

def teste8():
  idades = [15, 87, 32, 65, 56, 32, 49, 37]
  print(sorted(idades, reverse=True))

def teste9():
  idades = [15, 87, 32, 65, 56, 32, 49, 37]
  idades.sort()
  print(idades)

def teste10():
  nomes = [
    "guilherme",
    "Daniela",
    "Paulo",
  ]
  print(sorted(nomes))

if __name__ == '__main__':
  teste10()