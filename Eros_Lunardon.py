import random

impossible = False

def forca():
                global vidas
                if vidas > 6:
                    print("  _________")
                    print(" |         |      ")
                    print(" |                ")
                    print(" |         O      ")
                    print(" |        /|\     ")
                    print(" |________/ \     ")
                elif vidas == 6:
                    print("  _________")
                    print(" |         |")
                    print(" |          ")
                    print(" |")
                    print(" |")
                    print(" |___")
                elif vidas == 5:
                    print("  _________")
                    print(" |         |")
                    print(" |         O")
                    print(" |")
                    print(" |")
                    print(" |___")
                elif vidas == 4:
                    print("  _________")
                    print(" |         |")
                    print(" |         O")
                    print(" |         |")
                    print(" |")
                    print(" |___")
                elif vidas == 3:
                    print("  _________")
                    print(" |         |")
                    print(" |         O")
                    print(" |        /|")
                    print(" |")
                    print(" |___")
                elif vidas == 2:
                    print("  _________")
                    print(" |         |")
                    print(" |         O")
                    print(" |        /|\\")
                    print(" |")
                    print(" |___")
                elif vidas == 1:
                    print("  _________")
                    print(" |         |")
                    print(" |         O")
                    print(" |        /|\\")
                    print(" |        /")
                    print(" |___")
                elif vidas == 0:
                    print("  _________")
                    print(" |         |")
                    print(" |         O")
                    print(" |        /|\\")
                    print(" |        / \\")
                    print(" |___        ")
def escolhaDificuldade(palavras):
    global impossible
    if impossible == False:
        dificuldades = {"facil": 6, "medio": 4, "dificil": 2, "impossivel": 1}
    else:
         dificuldades = {"brasil":999, "facil": 6, "medio": 4, "dificil": 2, "impossivel": 1}

    # Pedir ao usuário para escolher a dificuldade
    if impossible == False:
        dificuldadeEscolhida = input("Escolha a dificuldade (facil/medio/dificil/impossivel): ").lower()
    else:
          dificuldadeEscolhida = input("Escolha a dificuldade (brasil/facil/medio/dificil/impossivel): ").lower()
    # Verificar se a dificuldade escolhida é válida
    if dificuldadeEscolhida not in dificuldades:
        print("Dificuldade inválida. Escolha entre facil, medio, dificil ou impossivel.")
    else:
       vidas,palavra_oculta, palavra = escolherPalavra(dificuldades,  dificuldadeEscolhida, palavras)
    
    return vidas, palavra_oculta, palavra, dificuldadeEscolhida, impossible


         
def escolherPalavra(dificuldades,dificuldadeEscolhida,palavras):
    palavra = random.choice(palavras).lower().strip()

        # Criar a palavra oculta
    palavra_oculta = "_" * len(palavra)

        # Obter o número de vidas para a dificuldade escolhida
    vidas = dificuldades[dificuldadeEscolhida]

    return vidas, palavra_oculta, palavra

while True:

    # Abrir arquivo de palavras e ler as palavras para uma lista
    with open("forca.txt", "r") as arquivo:
        palavras = arquivo.readlines()
        vidas, palavra_oculta, palavra, dificuldadeEscolhida, impossible = escolhaDificuldade(palavras)
        # Iniciar o jogo
        letras_inseridas = set()
        while "_" in palavra_oculta and vidas > 0:
            forca()
            print("\nPalavra:", palavra_oculta)
            letra = input("Adivinhe uma letra: \n").lower()
            letras_inseridas.add(letra)
            print("\nLetras já inseridas:", ', '.join(letras_inseridas))
            if len(letra) > 1:
                 if letra == palavra:
                      for i in range(len(palavra)):
                         palavra_oculta = letra
                 else:
                    vidas = 0
            elif letra in palavra:
                # Atualizar a palavra oculta
                for i in range(len(palavra)):
                    if palavra[i] == letra:
                        palavra_oculta = palavra_oculta[:i] + letra + palavra_oculta[i+1:]
            else:
                # Reduzir o número de vidas
                vidas -= 1
                print("Errou! Vidas restantes:", vidas)
                forca()
                
                
        # Exibir a mensagem de resultado
        if "_" not in palavra_oculta:
            print("  _________")
            print(" |         |")
            print(" |          ")
            print(" |           PARABENS!   ")
            print(" |         VOCÊ SOBREVIVEU ") # TOD
            print(" |___       AO DESAFIO     ")
            if dificuldadeEscolhida == "impossivel" and impossible == False:
                 print("Nova dificuldade desbloquada")
                 impossible = True
           
        else:
            print("\nVocê perdeu! A palavra era:", palavra)

    # Perguntar se o usuário quer jogar novamente
    jogar_novamente = input("\nQuer jogar novamente? (sim/nao): ").lower()
    if jogar_novamente != "sim":
        break
    print("Obrigado por jogar!")


    