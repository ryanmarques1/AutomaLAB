def create_afnafd(caracteres_especiais):
    import base
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
            if estados == caracteres_especiais:
                print("Vazio ou está com caracteres não permitidos, retornando ao menu de opções.")
                return

            print('Informe a linguagem do automato: ', end="")
            alfabeto = input().split()
            if alfabeto == caracteres_especiais:
                print("Vazio, retornando ao menu de opções.")
                return

            print('Informe o estado inicial: ', end="")
            estado_ini = input()
            if estado_ini == caracteres_especiais:
                print("Vazio, retornando ao menu de opções.")
                return

            print('Informe o(s) estado(s) finai(s): ', end="")
            estados_finais = input().split()
            if estados_finais == caracteres_especiais:
                print("Vazio, retornando ao menu de opções.")
                return

            print('Defina o delta(transição funções)', end="\n")

            for estado in estados:
                for simbolo in alfabeto:
                    print(f"\t {simbolo}")
                    print(f"{estado}\t------>\t", end="")
                    estado_prox = input().split()
                    
                    if  estado_prox == caracteres_especiais:
                        print("Vazio ou esta com caracteres especiais, retornando ao menu de opções.")
                        return
                    
                    if estado_prox == '-': #if para tratar casos onde um estado não atende um simbolo
                        delta[(estado, simbolo)] = None 
                    else:
                        delta[(estado, simbolo)] = estado_prox #armazenando o automato

            
        #---------------------Armazenando em arquivo o AFD criado em uma pasta generica (para utilizações posteriores)------------#
            pasta_afd = "AFDs/"
            if not os.path.exists(pasta_afd):
                os.mkdir(pasta_afd) #cria a pasta
            arq_automatoAFD = base.armazena_arquivo(pasta_afd, delta)
            arq_automatoAFD.close()
            
            delta_lista = base.dict_lista(delta) #convertendo o dicionario em uma lista de tuplas para plotagem.
            
            #Plotando
            AutomatoAFD = base.desenhar_automato(estado_ini,estados_finais,delta_lista)
            AutomatoAFD.render(pasta_afd + ('automatoAFD'), format='png', cleanup=True) #função cleanup serve para limpar para inserir outro automato.
            #Plotando
        elif op_create == 2:
            print("Criando um AFN", end="\n")
            print('Informe o conjunto de estados: ', end="")
            estados = input().split()
            if estados == caracteres_especiais:
                print("Vazio ou está com caracteres não permitidos, retornando ao menu de opções.")
                return

            print('Informe a linguagem do automato: ', end="")
            alfabeto = input().split()
            if alfabeto == caracteres_especiais:
                print("Vazio, retornando ao menu de opções.")
                return

            print('Informe o estado inicial: ', end="")
            estado_ini = input()
            if estado_ini == caracteres_especiais:
                print("Vazio, retornando ao menu de opções.")
                return

            print('Informe o(s) estado(s) finai(s): ', end="")
            estados_finais = input().split()
            if estados_finais == caracteres_especiais:
                print("Vazio, retornando ao menu de opções.")
                return
            
            for estado in estados:
                for simbolo in alfabeto:
                    print(f"\t {simbolo}")
                    print(f"{estado}\t------>\t", end="")
                    estado_prox = [prox for prox in input().split()] #estado_prox vira uma lista, o for opera em cima da função .split()
                    
                    if  estado_prox == caracteres_especiais:
                        print("Vazio ou esta com caracteres especiais, retornando ao menu de opções.")
                        return
                    
                    if estado_prox == '-': #if para tratar casos onde um estado não atende um simbolo
                        delta[(estado, simbolo)] = None 
                    else:
                        delta[(estado, simbolo)] = estado_prox #armazenando o automato
            
            pasta_afn = "AFNs/"
            if not os.path.exists(pasta_afn):
                os.mkdir(pasta_afn)
                
            arq_automatoAFN = base.armazena_arquivo(pasta_afn, delta)
            arq_automatoAFN.close()

            delta_novo = base.dict_lista(delta)

            # Plotando
            AutomatoAFN = base.desenhar_automato(estado_ini, estados_finais, delta_novo)
            AutomatoAFN.render(pasta_afn + ('automatoAFN'), format='png', cleanup=True)
            # Plotando
            
        elif op_create == 3:
            print("Informe a linguagem a ser reconhecida: ", end="") 
            entrada = input()
            estados_atuais = [estado_ini]
            
            for simbolo in entrada:
                print(f"Estados atuais: {estados_atuais}")
                novos_estados = []
                
                for estado_atual in estados_atuais:
                    prox_estados = delta.get((estado_atual, simbolo), [])
                    novos_estados.extend(prox_estados)
                    
                estados_atuais = novos_estados
                
                print(f"Entrada atual: {simbolo}")
                print(f"Próximos estados: {estados_atuais}")
            
            if any(estado in estados_finais for estado in estados_atuais):
                print("Reconheceu!")
            else:
                print("Não reconheceu!")
            
        elif op_create == 4:
            print("Voltando para o menu principal.", end="\n")
            break