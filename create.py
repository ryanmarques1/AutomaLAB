def create_afnafd():
    import os
    estados = []
    alfabeto = [] # 'a , b , c'
    delta = {} #Funções de transição dicionarios.
    estado_ini = ""
    estados_finais = []

    while 1:
        print("Menu de opções",end="\n")
        print('1. Criar AFD',end="\n")
        print('2. Criar um AFN',end="\n")
        print('3. Testar linguagem no AFD ou AFN',end="\n")
        print('4. Sair',end="\n")
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

        #---------------------Armazenando em arquivo o AFD criado em uma pasta generica (para utilizações posteriores)------------#
            pasta_afd = "AFDs/"
            if not os.path.exists(pasta_afd):
                os.mkdir(pasta_afd) #cria a pasta
            arq_automato = open(pasta_afd + ("automatoAFD_criado.txt"), 'w')# coloca o arquivo dentro da pasta
            arq_automato.writelines(str(delta)) #converte o dicionario porque metodos referentes a arquivos só aceitam strings.
            arq_automato.close()
            
        elif op_create == 2:
            print("Criando um AFN", end="\n")

        elif op_create == 3:
            print("Informe a linguagem a ser reconhecida: ", end="") 
            entrada = input()
            
            estado_atual = estado_ini
            
            for simbolo in entrada:
                print(f"Estado atual: {estado_atual}")
                print(f"Entrada atual: {simbolo}")
                
                proximo_estado = delta.get((estado_atual, simbolo))
                
                if proximo_estado is None:
                    print("O automato nao reconheceu a linguagem")
                    break
            
                estado_atual = proximo_estado
                print(f"Proximo estado: {estado_atual}")
            
            if estado_atual in estados_finais:
                print("Reconheceu!")
            else:
                print("Nao reconheceu!")
            
                
        elif op_create == 4:
            print("Voltando para o menu principal.", end="\n")
            break
        