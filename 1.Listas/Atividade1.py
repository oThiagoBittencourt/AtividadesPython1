'''
Atividade 2 -
    Crie uma versão do jogo da velha 4x4. As regras são as mesmas da versão 3x3.

        Obs: a entrada de linhas e colunas pelos jogadores é de base 0
'''

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

# é no game onde toda a inicialização do jogo é feita, as variaveis definidas, e onde o jogo acontece, até que chegue ao final. É por ele que as demais funções serão chamadas.
def game():
    # inicializações de variáveis
    ganhou = False
    jogada = 0
    tabuleiro = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    dimensoes = 4

    while not ganhou:
        # verifica se o jogo empatou
        if jogada == dimensoes * dimensoes:
            print("\nO jogo empatou!\n")
            break

        # tentativa do jogador
        jogador = "A" if jogada%2 == 0 else "B"
        print(f"\nJogada: {jogada}\nVez do jogador: {jogador}\n")
        exibir_tabuleiro(tabuleiro, dimensoes)

        print()
        try:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            # verifica se é possível executar a tentativa, e caso seja positivo adiciona
            if tabuleiro[linha][coluna] == 0:
                tabuleiro[linha][coluna] = 1 if jogador == "A" else -1
                jogada += 1
            else:
                print("Não é possível jogar nessa posição!")
        except:
            print("Insira um valor válido!")

        # verifica se o jogador venceu
        if(verificacao(tabuleiro, dimensoes)):
            print(f"\nO jogador {jogador} venceu!\n")
            break

# é na verificacao onde cada rodada do jogo é processada, para analisar se o jogo emaptou, ou se há um vencedor.
def verificacao(tabuleiro:list, dimensao:int):
    # verificar linhas
    for linha in tabuleiro:
        soma = 0
        for i in linha:
            soma += i
        if soma == (dimensao or (dimensao * -1)):
            return True
        
    # verificar colunas
    for i in range(dimensao):
        soma = 0
        for linha in tabuleiro:
            soma += linha[i]
        if soma == (dimensao or (dimensao * -1)):
            return True
        
    #verificar diagonais
    somaDiagonal0 = 0
    somaDiagonal1 = 0
    for i in range(dimensao):
        somaDiagonal0 += tabuleiro[i][i]
        somaDiagonal1 += tabuleiro[i][(dimensao -1) - i]
    if somaDiagonal0 == (dimensao or (dimensao * -1)) or somaDiagonal1 == (dimensao or (dimensao * -1)):
        return True
    return False

# exibir_tabuleiro é a função onde é impresso no console a visualizção do tabuleiro.
def exibir_tabuleiro(tabuleiro:list, dimensao:int):
    for i in range(dimensao):
        for j in range(dimensao):
            if tabuleiro[i][j] == 1:
                print(" X ", end = ' ')
            elif tabuleiro[i][j] == -1:
                print(" O ", end = ' ')
            else:
                print(" _ ", end = ' ')
        print()

menu()