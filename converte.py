import base

from graphviz import Digraph
def converte_afn_afd():
    pasta_afn = "AFNs/"
    pasta_afd = "AFDs/"

   # res = base.verifica_existencia(pasta_afn)
    estado_inicial = None
    estados_finais = []
    alfabeto = []
    # Carrega a tabela de transições do AFN
    delta_afn = base.converte_txt_dict(pasta_afn)
    
        
    # Carrega os estados finais, alfabeto e estado inicial do AFN
    estado_inicial, estados_finais, alfabeto = base.push_ini_fini_alfabeto(pasta_afn, estado_inicial, estados_finais, alfabeto)
    
    estado_ini = [estado_inicial]  # Estado inicial como lista
    # Obtém os estados do AFN
    #estados = base.retorna_estados(pasta_afn)
    
    # Inicializa o estado inicial do AFD
    estados_afd = []  # Conjunto de estados do AFD
    tabela_transicoes_afd = {}  # Dicionário para armazenar a tabela de transições
    estados_finais_afd = []

    # Inicializa a fila de estados a serem processados 
    fila = [estado_ini]

    while fila:
        estados_atual = fila.pop(0)

        if estados_atual not in estados_afd:
            estados_afd.append(estados_atual)

        for simbolo in alfabeto:
            # Conjunto de estados para o próximo estado AFD
            proximo_estado = []

            for estado in estados_atual:
                if (estado, simbolo) in delta_afn:
                    for e in delta_afn[(estado, simbolo)]:
                        if e not in proximo_estado:
                            proximo_estado.append(e)
            
            if proximo_estado:
                if proximo_estado not in estados_afd:
                    fila.append(proximo_estado)
                
                estado_a = "".join(estados_atual)
                estado_p = "".join(proximo_estado)
                tabela_transicoes_afd[(estado_a, simbolo)] = estado_p
        # Verifica se o estado atual é um estado final do AFD
        if any(estado in estados_finais for estado in estados_atual):
            estados_finais_afd.append(estado_a)
    #print(estados_afd)

    # Salva o AFD em um arquivo
    #estados = list(map(lambda sub: ''.join(sub), estados_afd))
    estados = [''.join(estado) for estado in estados_afd]

    arq = open(pasta_afd + ('estados.txt'), 'w+')
    arq.writelines('\n'.join(estados))

    
    #print(delta_afn)
    #print("------------------")
    #print(tabela_transicoes_afd)
    
    base.armazena_informacoes(pasta_afd, estado_inicial, estados_finais_afd, alfabeto)
    base.armazena_arquivo(pasta_afd, tabela_transicoes_afd)
    print(estados_finais_afd)
    automato = Digraph() #Definindo que a var automato é do tipo Digraph()
    automato.attr(rankdir='LR') #LR siginifica da esquerda para direita. entao o automato será criado usando essa regra
    automato.attr('node', shape='circle') #definindo os atributos do node (nós)
    
    
    automato.node('->', shape='none', width='0', heigth='0',label='')
    automato.edge('->', estado_inicial)
    
    for estado_final in estados_finais_afd: 
        automato.node(estado_final, shape='doublecircle', fontsize='19', fontcolor='green')#colocando circulo duplo em todos os estados finais.
    for (estado, simbolo) in tabela_transicoes_afd:
            destino = tabela_transicoes_afd[(estado, simbolo)]
            automato.edge(estado,destino,label=simbolo) #edge insere as setas de acordo com o delta, label = simbolo siginica que em cima da seta estará o simbolo.
    automato.render(pasta_afd + ('AutomatoConvertido'), format='png', cleanup=True)

    aux_alfa = alfabeto.split()
    delta_afd = {key: [value] for key, value in tabela_transicoes_afd.items()} # AQUI eu transformo meu valor da key em uma lista, para adaptar para o codgio de testar linguagem

    #acho que desta forma consigo corrigir outro bug da minimização.
    
    print(delta_afd)
    #Equivalencia
    print("Deseja testar equivalência do AFN e AFD convertido? S-SIM/N-NÃO")
    res = input()
    if res == 'S':
        print("Digite o tamanho do teste: (Min = 1 Max = ATÉ ONDE CONSEGUIR)\n")
        tam_equivalencia = int(input())
        cont = cont2 = cont3 = cont4 = 0
        
            
        for _ in range(tam_equivalencia):
            entrada = base.gerarEntradaAleatoria(aux_alfa)
            print(entrada)
            estados_atuais = [estado_inicial]
            for simbolo in entrada:
                    print(f"Estados atuais: {estados_atuais}")
                    novos_estados = []
                
                    for estado_atual in estados_atuais:
                        prox_estados = delta_afn.get((estado_atual, simbolo), [])
                        novos_estados.extend(prox_estados)
                    
                    estados_atuais = novos_estados
                
            print(f"Entrada atual: {simbolo}")
            print(f"Próximos estados: {estados_atuais}")
            
            if any(estado in estados_finais for estado in estados_atuais):
                cont = cont + 1
                print("Reconheceu!")
            else:
                cont2 = cont2 - 1
                print("Não reconheceu!")
            
            print("/-----------------------------------------------------/")
            estados_atuais2 = [estado_inicial]
            for simbolo in entrada:
                    print(f"Estados atuais: {estados_atuais2}")
                    novos_estados2 = []
                
                    for estado_atual2 in estados_atuais2:
                        prox_estados2 = delta_afd.get((estado_atual2, simbolo), [])
                        novos_estados2.extend(prox_estados2)
                    
                    estados_atuais2 = novos_estados2
                
            print(f"Entrada atual: {simbolo}")
            print(f"Próximos estados: {estados_atuais2}")
            
            if any(estado in estados_finais_afd for estado in estados_atuais2):
                cont3 = cont3 + 1
                print("Reconheceu!")
            else:
                cont4 = cont4 - 1
                print("Não reconheceu!")
        if cont == cont3 or cont2 == cont4:
            print("\nSão equivalentes\n")
        else:
            print("\nNão são")




