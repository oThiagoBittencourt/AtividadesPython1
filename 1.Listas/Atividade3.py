'''
Atividade 3 -
    Desenvolver o jogo https://term.ooo/ a partir do arquivo lista_palavras.txt. O jogo deve ser
    jogado por meio do terminal, mantendo a lógica do jogo original. Devem aparecer as letras que
    já foram descobertas, as letras já tentadas no teclado e assim por diante. Atente-se à
    formatação.
'''

import random

# menu é a parte da navegação do usuário onde o mesmo deve escolher entre a opção de jogar ou encerrar o programa.
def menu():
    while True:
        try:
            entrada = int(input("0. Iniciar Jogo\n" + "1. Sair\n"))
        except:
            print("Insira um valor válido!\n")
        else:
            if entrada == 0:
                game()
            elif entrada == 1:
                print("Saindo...")
                break
            else:
                print("Insira um valor válido!\n")

# função para ler o arquivo .txt de palavras e transformar em uma lista
def le_arquivo(arq):
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f]
    
# função principal, onde a palavra é sorteada, e o controle das tentativas, acertos e erros é realizada.
def game():
    palavra = random.choice(le_arquivo("lista_palavras.txt"))
    letrasCorretas = []
    letrasErradas = []
    tentativas = len(palavra)

    while True:
        # verifica se as tentativas acabaram
        if tentativas == 0:
            print("\nGame Over!\n")
            break
        else:
            # tentativas do usuário
            print(f"\nTentativas Restantes: {tentativas}")
            print(f"Letras erradas:", end=' ')
            print(*letrasErradas, sep=', ')
            exibir(palavra, letrasCorretas)

            entrada = input("Insira uma tentativa:\n")
            if len(entrada) != len(palavra):
                print("\nInsira uma palavra com a mesma quantidade de caracteres!")
                continue

            # verifica se a letra pertence a aquele índice
            for i in range(len(palavra)):
                if palavra[i] == entrada[i]:
                    if not letrasCorretas.count(i):
                        letrasCorretas.append(i)
                else:
                    if not palavra.count(entrada[i]):
                        if not letrasErradas.count(entrada[i]):
                            letrasErradas.append(entrada[i])
            
            # verifica se o jogador venceu
            if len(letrasCorretas) == len(palavra):
                print(f"\nVocê venceu!\nA palavra era: {palavra}\n")
                break
            tentativas -= 1

# função para printar para o usuário as letras conhecidas e desconhecidas da palavra
def exibir(palavra:str, letras:list):
    print("Palavra:")
    for i in range(len(palavra)):
        if letras.count(i):
            print(f"{palavra[i]}", end=' ')
        else:
            print("_", end=' ')
    print()

menu()