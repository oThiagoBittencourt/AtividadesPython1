'''
Atividade 4 -
    Crie um menu com três opções:
        1-cadastrar usuário
        2-imprimir usuários
        0-encerrar
            Ao iniciar, o programa deve solicitar ao usuário os nomes dos campos que serão obrigatórios
            para os cadastros.
            Na sequência, deve mostrar o menu e iniciar o fluxo normal de execução.
'''

bancoDados = {}

# é atrvés deste método que os campos obrigatórios para os usuários é definida ('nome' é padrão)
def definir_campos():
    camposObrigatorios = []
    while True:
        print()
        try:
            entrada = int(input("1. Inserir Campo Obrigatório\n" + "2. Iniciar Programa\n" + "0. Sair\n"))
        except:
            print("Insira um valor válido!\n")
        else:
            if entrada == 1:
                camposObrigatorios.append(input("Insira um Campo Obrigatório ao Sistema: "))
            elif entrada == 2:
                menu(camposObrigatorios)
                break
            elif entrada == 0:
                print("Saindo...")
                break
            else:
                print("Insira um valor válido!\n")

# no menu o usuário navegará entre as opções do sistema
def menu(camposObrigatorios:list):
    while True:
        print()
        try:
            entrada = int(input("1. Cadastrar Usuário\n" + "2. Imprimir Usuários\n" + "0. Sair\n"))
        except:
            print("Insira um valor válido!\n")
        else:
            if entrada == 1:
                cadastrar_usuario(camposObrigatorios)
            elif entrada == 2:
                imprimir_usuarios()
            elif entrada == 0:
                print("Saindo...")
                break
            else:
                print("Insira um valor válido!\n")

# é aqui onde o usuário irá de fato inserir um cadastro, caso todos os campos obrigatórios sejam respeitados
def cadastrar_usuario(*camposObrigatorios):
    campos = {}
    nome = input("Insira o nome do cliente: ")
    while True:
        print()
        try:
            print(f"Campos necessários restantes:", end=' ')
            for i in camposObrigatorios:
                for j in i:
                    if not campos.get(j):
                        print(j, end=', ')
            print()

            chave = input("Insira uma chave: ")
            if chave.lower() == "sair":
                break
            valor = input("Insira uma chave: ")
            if valor.lower() == "sair":
                break
        except:
            print("Insira um valor válido!\n")
        else:
            if not campos.get(chave):
                campos[chave] = valor
                print(f"{chave} = {campos[chave]}")
            else:
                print("Chave já existente!\n")
    for i in camposObrigatorios:
        for j in i:
            if not campos.get(j):
                print("\nNão foi possível realizar o cadastro: Você não inseriu todos os campos obrigatórios!")
                return
    bancoDados[nome] = campos

# através desta função que o usuário conseguirá ver os clientes anteriormente adicionados ao sistema, através de buscas de campos controláveis
def imprimir_usuarios():
    while True:
        try:
            entrada = int(input("\n1. Imprimir Todos\n" + "2. Filtrar por Nomes\n" + "3. Filtrar por Campos\n" + "4. Filtrar por Nomes e Campos\n"))
        except:
            print("Insira um valor válido!\n")
        else:
            match entrada:
                # imprimir todos
                case 1:
                    print("\nResultados:")
                    for nome in bancoDados:
                        print(f"{nome} = {bancoDados[nome]}")
                    return
                # imprimir através dos nomes
                case 2:
                    nomes = input("\nInsira os nomes para pesquisa (ex: João, Maria, Paulo): ").split(', ')
                    print("\nResultados:")
                    for nome in bancoDados:
                        if nomes.count(nome):
                            print(f"{nome} = {bancoDados[nome]}")
                    return
                # imprimir através dos campos
                case 3:
                    nomes_temp = []
                    for nome in bancoDados:
                        nomes_temp.append(nome)
                    while True:
                        chave = input("\nInsira o campo de busca: ")
                        if chave.lower() == "sair":
                            break
                        valor = input(f"Insira o valor desejado de {chave}: ")
                        if valor.lower() == "sair":
                            break
                        for nome in nomes_temp:
                            controlador = False
                            for item in bancoDados[nome]:
                                if item == chave and valor == bancoDados[nome][item]:
                                    controlador = True
                                    break
                            if not controlador:
                                nomes_temp.remove(nome)
                    for nome in nomes_temp:
                        print("\nResultados:")
                        print(f"{nome} = {bancoDados[nome]}")
                    return
                # imprimir através dos nomes e campos
                case 4:
                    nomes = input("\nInsira os nomes para pesquisa (ex: João, Maria, Paulo): ").split(', ')
                    nomes_temp = nomes
                    while True:
                        chave = input("\nInsira o campo de busca: ")
                        if chave.lower() == "sair":
                            break
                        valor = input(f"Insira o valor desejado de {chave}: ")
                        if valor.lower() == "sair":
                            break
                        for nome in nomes_temp:
                            if not bancoDados.get(nome):
                                break
                            controlador = False
                            for item in bancoDados[nome]:
                                if item == chave and valor == bancoDados[nome][item]:
                                    controlador = True
                                    break
                            if not controlador:
                                nomes_temp.remove(nome)
                    print("\nResultados:")
                    for nome in nomes_temp:
                        print(f"{nome} = {bancoDados[nome]}")
                    return
                case _:
                    print("Insira um valor válido!\n")

definir_campos()