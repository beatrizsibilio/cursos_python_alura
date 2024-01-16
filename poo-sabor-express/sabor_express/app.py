from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
from modelos.restaurante import Restaurante


restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_pave = Sobremesa('Pavê', 20.0, 'Pavê de leite ninho com nutela', 'Doce', 'Médio')
sobremesa_pave.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_pave)


def main():
  restaurante_praca.exibir_cardapio


if __name__ == '__main__':
  main()