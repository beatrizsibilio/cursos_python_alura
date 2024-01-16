import array as arr

class Conta:
  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0
  
  def deposita(self, valor):
    self.saldo += valor
  
  def __str__(self):
    return "[>>Código {} Saldo {}<<]".format(self.codigo, self.saldo)
  
conta_do_gui = Conta(15)
print(conta_do_gui)
conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = Conta(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
  print(conta)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]
print(contas[0])

conta_do_gui.deposita(100)
print(contas[0])

print(contas[2])
contas[2].deposita(300)
print(conta_do_gui)


def deposita_para_todas(contas):
  for conta in contas:
    conta.deposita(100) 

contas = [conta_do_gui, conta_da_dani]
print("\n",contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0,76)
print(contas[0], contas[1], contas[2])

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

conta_do_gui = (15, 1000)

def deposita(conta): #variação "funcional"
  novo_saldo  = conta[1] + 100
  codigo = conta[0]
  return(codigo, novo_saldo )

conta_do_gui = deposita(conta_do_gui)
print(conta_do_gui)

usuarios = [guilherme, daniela]
print(usuarios)
usuarios.append(('Paulo', 39, 1979))
print(usuarios)

conta_do_gui = Conta(15)
conta_do_gui.deposita(500)
conta_da_dani = Conta(234876)
conta_da_dani.deposita(1000)
contas = (conta_do_gui, conta_da_dani)
print(contas)

contas[0].deposita(300)

for conta in contas:
  print(conta)

class ContaCorrente(Conta):
  def passa_o_mes(self):
    self.saldo -= 2

class ContaPoupanca(Conta):
  def passa_o_mes(self):
    self.saldo *= 1.01
    self.saldo -= 3

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
  conta.passa_o_mes()
  print(conta)

arr.array('d', [1, 3.5])

conta_do_gui = Conta(15)
conta_do_gui.deposita(500)
conta_da_dani = Conta(234876)
conta_da_dani.deposita(1000)

from operator import attrgetter
for conta in sorted(contas, key=attrgetter("_saldo")):
  print(conta)