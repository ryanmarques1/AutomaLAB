def minimiza_afd():
    import base
    from graphviz import Digraph
    
    pasta_afd = "AFDs/"
    estado_ini = ''
    estados_finais = []
    alfabeto = []

    #res = base.verifica_existencia(pasta_afd)
    delta_afd = base.converte_txt_dict(pasta_afd)
    estados = base.retorna_estados(pasta_afd)
    estado_ini, estados_finais, alfabeto = base.push_ini_fini_alfabeto(pasta_afd, estado_ini, estados_finais, alfabeto)

    
    tabela_minimiza = {}
    alterado = True
    combina_estados = {}
    novos_estados_finais = []
    novo_delta_afd = {}
    novos_estados = []


    print(estados)
    # Inicializar a tabela de minimizacao
    for s1 in estados:
        for s2 in estados:
            if s1 != s2:
                tabela_minimiza[(s1, s2)] = (s1 in estados_finais) != (s2 in estados_finais)
            else:
                tabela_minimiza[(s1,s2)] = True
    
    #Marcar as estados nao iguais
    while alterado:
        alterado = False
        for (s1, s2), distinto in tabela_minimiza.items():
            if not distinto:
                for simbolo in {simbolo for (estado, simbolo) in delta_afd.keys()}:
                    destino1 = delta_afd.get((s1, simbolo), [None])[0]
                    destino2 = delta_afd.get((s2, simbolo), [None])[0]
                    if destino1 and destino2 and (destino1 != destino2):
                        if tabela_minimiza.get((destino1, destino2), False) or tabela_minimiza.get((destino2, destino1), False):
                            tabela_minimiza[(s1, s2)] = True
                            alterado = True
                            break
    
    #Marcar estados
    for (s1, s2), distinto in tabela_minimiza.items():
        
        if not distinto:
            
            combina_estados[s1] = tabela_minimiza.get(s1, s1)
            combina_estados[s2] = tabela_minimiza.get(s1, s1)
    
    #novos estados finais
    print(tabela_minimiza)
    for estado in estados_finais:
        novo_estado = combina_estados.get(estado, estado)
        print(novo_estado)
        if novo_estado not in novos_estados_finais:
          novos_estados_finais.append(novo_estado) # Problema aqui
        

    
    # gerando novo delta_afd
    
    
    for (estado, simbolo), destinos in delta_afd.items():
        novo_estado = combina_estados.get(estado, estado)
        novo_destino = combina_estados.get(destinos[0], destinos[0])
        novo_destino_a = "".join(novo_destino)
        novo_delta_afd[(novo_estado, simbolo)] = novo_destino_a
    
    
    for estado in estados:
        novo_estado = combina_estados.get(estado, estado)
        print(novo_estado)
        if novo_estado not in novos_estados:
            novos_estados.append(novo_estado)

    novo_estado_inicial = combina_estados.get(estado_ini, estado_ini)
    
    
    
    automato = Digraph() #Definindo que a var automato é do tipo Digraph()
    automato.attr(rankdir='LR') #LR siginifica da esquerda para direita. entao o automato será criado usando essa regra
    automato.attr('node', shape='circle') #definindo os atributos do node (nós)
    
    automato.node('', shape='none')
    automato.edge('', novo_estado_inicial)
    
    #print(novo_delta_afd)
    for estado in novos_estados:
        if estado in estados_finais:
            automato.node((estado), shape='doublecircle', fontsize='19', fontcolor='green')

    for (estado, simbolo) in novo_delta_afd:
            destino = novo_delta_afd[(estado, simbolo)]
            automato.edge(estado,destino,label=simbolo) #edge insere as setas de acordo com o delta, label = simbolo siginica que em cima da seta estará o simbolo.
    automato.render(pasta_afd + ('AutomatoMinimizado'), format='png', cleanup=True)

    