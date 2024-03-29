import random

def jogar():
	imprime_mensagem_abertura()
	palavra_secreta = carregar_palavra_secreta()
	letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
	print(letras_acertadas)

	enforcou = False
	acertou = False
	erros = 0 

	while(not enforcou and not acertou):

		chute = inicializar_chute()

		if(chute in palavra_secreta):
			marcar_chute_correto(chute, palavra_secreta, letras_acertadas)
		else:
			erros += 1
			print("Ops, você errou! Faltam {} tentativas.".format(7-erros))
			desenha_forca(erros)

		enforcou = 7 == erros
		acertou = "_" not in letras_acertadas
		print(letras_acertadas)

	if(acertou):
		imprime_mensagem_vencedor()
	else:
		imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
	print("*********************************")
	print("***Bem vindo ao jogo de forca!***")
	print("*********************************")

def carregar_palavra_secreta():
	with open("palavras.txt", "r") as arquivo:
		palavras = []

		for linha in arquivo:
			linha = linha.strip().upper()
			palavras.append(linha)

	numero = random.randrange(0, len(palavras))
	palavra_secreta = palavras[numero]

	return palavra_secreta

def inicializar_letras_acertadas(palavra):
	return ["_" for letra in palavra]

def inicializar_chute():
	chute = input("Qual letra? ")
	chute = chute.strip().upper()
	return chute

def marcar_chute_correto(chute, palavra_secreta, letras_acertadas):
	index = 0
	for letra in palavra_secreta:
		if(chute == letra):
			letras_acertadas[index] = letra	
		index += 1

def desenha_forca(erros):
	print("  _______     ")
	print(" |/      |    ")

	if(erros == 1):
			print(" |      (_)   ")
			print(" |            ")
			print(" |            ")
			print(" |            ")

	if(erros == 2):
			print(" |      (_)   ")
			print(" |      \     ")
			print(" |            ")
			print(" |            ")

	if(erros == 3):
			print(" |      (_)   ")
			print(" |      \|    ")
			print(" |            ")
			print(" |            ")

	if(erros == 4):
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |            ")
			print(" |            ")

	if(erros == 5):
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |       |    ")
			print(" |            ")

	if(erros == 6):
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |       |    ")
			print(" |      /     ")

	if (erros == 7):
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |       |    ")
			print(" |      / \   ")

	print(" |            ")
	print("_|___         ")
	print()

def imprime_mensagem_vencedor():
	print("Parabéns, você ganhou!")
	print("       ___________      ")
	print("      '._==_==_=_.'     ")
	print("      .-\\:      /-.    ")
	print("     | (|:.     |) |    ")
	print("      '-|:.     |-'     ")
	print("        \\::.    /      ")
	print("         '::. .'        ")
	print("           ) (          ")
	print("         _.' '._        ")
	print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
	print("Puxa, você foi enforcado!")
	print("A palavra era {}".format(palavra_secreta))
	print("    _______________         ")
	print("   /               \       ")
	print("  /                 \      ")
	print("//                   \/\  ")
	print("\|   XXXX     XXXX   | /   ")
	print(" |   XXXX     XXXX   |/     ")
	print(" |   XXX       XXX   |      ")
	print(" |                   |      ")
	print(" \__      XXX      __/     ")
	print("   |\     XXX     /|       ")
	print("   | |           | |        ")
	print("   | I I I I I I I |        ")
	print("   |  I I I I I I  |        ")
	print("   \_             _/       ")
	print("     \_         _/         ")
	print("       \_______/           ")

if(__name__ == "__main__"):
	jogar()