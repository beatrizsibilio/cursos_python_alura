import os

restaurantes = [
  {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
  {'nome': 'Pizza Suprema', 'categoria': 'Pizzas', 'ativo': True},
  {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]

def exibir_nome_programa():
  ''' Essa função é responsável por exibir o título do programa '''
  print(''' 
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def exibir_opcoes():
  ''' Essa função é responssável por exibir as opções de atividades do programa'''
  print('1. Cadastrar restaurante')
  print('2. Listar restaurante')
  print('3. Alternar estado do restaurante')
  print('4. Sair\n')

def finalizar_app():
  '''Essa funçaõ é responsável por finalizar o programa'''
  exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
  ''' Essa função é responsável por fazer o programa voltar á tela principal'''
  input('\nDigite uma tecla para voltar ao menu principal')
  main()

def opcao_invalida():
  ''' Essa função é responsável por declarar que foi digitada uma opção inválida'''
  print('Opção inválida\n')
  voltar_ao_menu_principal()

def exibir_subtitulo(texto):
  '''Essa função é responsavel por exibir os subtitulos das opções'''
  os.system('clear')
  linha = '*' * (len(texto))
  print(linha)
  print(texto)
  print(f'{linha}\n')

def cadastrar_novo_restaurante():
  ''' essa funçaõ é responsável por cadastrar um novo
  restaurante'''
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
  dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
  restaurantes.append(dados_do_restaurante)
  print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

  voltar_ao_menu_principal()

def listar_restaurantes():
  '''essa função é responsável por listar os restaurantes cadastrados'''
  exibir_subtitulo('Listando os restaurantes')
  print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = 'ativado' if restaurante['ativo'] else 'desativado'
    print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
  
  voltar_ao_menu_principal()

def alternar_estado_restaurante():
  '''Essa função é responsável por alternar o estado do restaurante'''
  exibir_subtitulo('Alternando estado do restaurante')
  nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
  restaurante_encontrado = False

  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo']
      mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)
  
  if not restaurante_encontrado:
    print('O restaurante não foi encontrado')
  voltar_ao_menu_principal()

def escolher_opcao():
  '''Essa função responsável pela escolha das opções do programa'''
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      alternar_estado_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

def main():
  os.system('clear')
  exibir_nome_programa()
  exibir_opcoes()
  escolher_opcao()


if __name__ == '__main__':
  main()