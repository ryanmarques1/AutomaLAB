def create_afnafd():
    estados = []
    alfabeto = []
    delta = {}
    estado_ini = ""
    estados_finais = []

    while 1:
        print('1. Criar AFD'
            '2. Criar AFN'
            '3. Testar linguagens'
            '4. Sair')
        op_create = int(input('Entre com a opcao desejada: '))
        if op_create == 1:
            print("Criando um AFD", end="\n")
            print('Informe o conjunto de estados: ', end="")
            estados = input().split()

            print('Informe a linguagem do automato: ', end="")
            alfabeto = input().split()

            print('Informe o estado inicial: ', end="")
            estado_ini = input()

            print('Informe o(s) estado(s) finai(s): ', end="")
            estados_finais = input().split()

            print('Defina o delta(transição funções)', end="\n")

            for estado in estados:
                for simbolo in alfabeto:
                    print(f"\t {simbolo}")
                    print(f"{estado}\t------>\t", end="")
                    estado_prox = input()
                    
                    if estado_prox == '-': #if para tratar casos onde um estado não atende um simbolo
                        delta[(estado, simbolo)] = None 
                    else:
                        delta[(estado, simbolo)] = estado_prox #armazenando o automato
            return
        elif op_create == 2:
            print("Criando um AFN", end="\n")

            print('Informe o conjunto de estados: ', end="")
            estados = input().split()

            print('Informe a linguagem do automato: ', end="")
            linguagem = input().split()

            print('Informe o estado inicial: ', end="")
            estado_ini = input()

            print('Informe o(s) estado(s) finai(s): ', end="")
            estados_finais = input().split()
            
            return
        elif op_create == 3:
            print("Testando linguagens", end="\n")
            print("Entre com a linguagem a ser testada: ", end="")
            linguagem_entrada = input()
            estado_atual = estado_ini

            for simbolo in linguagem_entrada:
                print(f"Estado atual: {estado_atual}")
                print(f"Entrada testada: {linguagem_entrada}")

                print(f"Proximo: {delta[(estado_atual,simbolo)]}")

                if estado_atual == None:
                    print("Error")
            if estado_atual in estados_finais:
                print("Deu certo")
            else:
                print("Erro")
            return
        
            
        