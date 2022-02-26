import random

cont = "s"

while cont == "s":

    # Palavras que podem aparecer na forca
    lista = (
        "afobado", "amendoim", "banheiro", "caatinga", "cachorro", "campeonato", "capricornio", "catapora", "corrupçao",
        "crepusculo", "empenhado", "esparadrapo", "forca", "galaxia", "historia", "magenta", "manjericao", "menta",
        "moeda",
        "oração", "paçoca", "palavra", "pedreiro", "pneumonia", "pulmao", "rotatoria", "serenata", "transeunte",
        "trilogia",
        "xicara"
    )

    palavra = random.choice(lista)
    digitadas = []
    vidas = 0

    # Introdução
    print("Olá, bem-vindo ao jogo da forca !")
    print("")
    print("REGRAS:")
    print("*O número de vidas inicial é determinado de acordo com a dificuldade")
    print("*Somente letras minúsculas são permitidas")
    print(f'*CUIDADO, "c" e "ç" são considerados diferentes')
    print("*Para ganhar descubra a palavra antes da suas vidas terminarem")
    print("*Se suas vidas acabarem, é GAME OVER")
    print("")

    # Seleção de dificuldade
    while True:
        dificuldade = input("Escolha o nível de dificuldade! 1-Fácil, 2-Normal 3-Difícil: ")

        if dificuldade == "1":
            vidas = 10
            break
        elif dificuldade == "2":
            vidas = 6
            break
        elif dificuldade == "3":
            vidas = 1
            print("Você é corajoso mesmo ein? Não pode errar nenhuma vez!!!")
            break
        else:
            print("Digite um número válido")
            continue

    print("")
    print("Ótimo, vamos começar:")
    print("")
    print(f'A palavra é: {len(palavra) * "*"}')
    print("")

    # Forca propriamente dita
    while True:

        # Final do jogo
        if vidas <= 0:
            print("GAME OVER !!")
            print(f'A palavra era {palavra.upper()}.')
            break

        letra = input('Digite uma letra: ')

        if len(letra) > 1:
            print('Por favor, só uma letra por vez.')
            continue

        digitadas.append(letra)

        if letra in palavra:
            print(f'a letra "{letra.upper()}" está correta.')
        else:
            print(f'Você errou ! Não tem "{letra.upper()}" na palavra.')
            digitadas.pop()

        secreto_temporario = ""
        for letra_secreta in palavra:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += "*"
        print(secreto_temporario)

        # GAME WIN
        if secreto_temporario == palavra:
            print(f'Parabéns !!!, a palavra era {palavra.upper()}.')
            break

        if letra not in palavra:
            vidas = vidas - 1
        if vidas > 1:
            print(f" Você ainda tem {vidas} vidas.")
            print()
        if vidas == 1:
            print(f" Você ainda tem {vidas} vida.")
            print()

    # Repetição de jogo
    while True:
        cont2 = input("Deseja jogar novamente? s/n: ")
        if cont2 == "s" or cont2 == "n":
            cont = cont2
            break
        else:
            print("Digite 's' ou 'n'")
            continue
