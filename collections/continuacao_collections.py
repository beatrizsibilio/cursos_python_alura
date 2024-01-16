def teste1():
  usuarios_datascience = [15, 23, 43, 56]
  usuarios_machine_learning = [13, 23, 56, 42]

  assistiram = usuarios_datascience.copy()
  assistiram.extend(usuarios_machine_learning)
  print(set(assistiram))

  for usuario in assistiram:
    print(usuario)


def teste2():
  usuarios_datascience = {15, 23, 43, 56}
  usuarios_machine_learning = {13, 23, 56, 42}

  print(usuarios_datascience | usuarios_machine_learning)
  print(usuarios_datascience & usuarios_machine_learning)
  print(usuarios_datascience - usuarios_machine_learning)

def teste3():
  usuarios_datascience = {15, 23, 43, 56}
  usuarios_machine_learning = {13, 23, 56, 42}

  fez_ds_nao_fez_ml = usuarios_datascience - usuarios_machine_learning
  print(15 in fez_ds_nao_fez_ml)
  print(23 in fez_ds_nao_fez_ml)

def teste4():
  usuarios = {1, 5, 76, 34, 52, 13, 17}
  print(len(usuarios))
  usuarios.add(13)
  print(len(usuarios))
  usuarios.add(765)
  print(len(usuarios))
  usuarios = frozenset(usuarios)
  print(usuarios)

def teste5():
  meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
  print(set(meu_texto.split()))

  aparicoes = {
    "Guillherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
  }

  print(aparicoes["Guillherme"])
  print(aparicoes["cachorro"])
  print(aparicoes.get("xpto", 0))
  print(aparicoes.get("cachorro", 0))

  aparicoes["Carlos"] = 1
  print(aparicoes)

  print("cachorro" in aparicoes)
  print("Carlos" in aparicoes)

  for elemento in aparicoes:
    print(elemento)
  
  for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

  for chave, valor in aparicoes.items():
      valor = aparicoes[elemento]
      print(chave, "=", valor)

from collections import Counter

def teste6():
  meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
  meu_texto = meu_texto.lower()
  aparicoes = Counter()
  for palavra in meu_texto.split():
    aparicoes[palavra] += 1
  print(aparicoes)

def teste7():
  meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
  meu_texto = meu_texto.lower()
  aparicoes = Counter(meu_texto.split())
  print(aparicoes)

if __name__ == '__main__':
  teste7()