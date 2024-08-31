def minimiza_afd():
    import base
    from graphviz import Digraph
    
    pasta_afd = "AFDs/"
    estado_ini = ''
    estados_finais = []
    alfabeto = []

    #res = base.verifica_existencia(pasta_afd)
    delta_afd = base.converte_txt_dict(pasta_afd)
    #delta_afd = {key: [value] for key, value in delta_afd.items()} #valor vira lista [ ] 
    
    print(delta_afd)
    estados = base.retorna_estados(pasta_afd)
    print(estados)
    estado_ini, estados_finais, alfabeto = base.push_ini_fini_alfabeto(pasta_afd, estado_ini, estados_finais, alfabeto)
    print(estado_ini)

    print(estados_finais)
    print(alfabeto)
    tabela_minimiza = {}
    alterado = True
    combina_estados = {}
    novo_delta_afd = {}
    novos_estados = []
    qn_estado = 'qn'


    # Inicializar a tabela de minimizacao
    for s1 in estados:
        for s2 in estados:
            if s1 != s2:
                tabela_minimiza[(s1, s2)] = (s1 in estados_finais) != (s2 in estados_finais)
            else:
                tabela_minimiza[(s1, s2)] = True
    
    # Marcar os estados não iguais
    while alterado:
        alterado = False
        for (s1, s2), distinto in tabela_minimiza.items():
            if not distinto:
                for simbolo in {simbolo for (estado, simbolo) in delta_afd.keys()}:
                    destinos1 = delta_afd.get((s1, simbolo), [None])
                    destinos2 = delta_afd.get((s2, simbolo), [None])
                    if destinos1 and destinos2 and destinos1[0] and destinos2[0]:
                        destino1 = destinos1[0]
                        destino2 = destinos2[0]
                        if destino1 != destino2:
                            if tabela_minimiza.get((destino1, destino2), False) or tabela_minimiza.get((destino2, destino1), False):
                                tabela_minimiza[(s1, s2)] = True
                                alterado = True
                                break
    
    # Marcar estados
    for (s1, s2), distinto in tabela_minimiza.items():
        if not distinto:
            combina_estados[s1] = combina_estados.get(s1, s1)
            combina_estados[s2] = combina_estados.get(s1, s1)

    #novos estados do afd minimizado

    for estado in estados:
        novo_estado = combina_estados.get(estado, estado)
        if novo_estado not in novos_estados:
            novos_estados.append(novo_estado)
    
    # Novos estados finais
    n_finais = []
    novos_estados_finais = []
    for s1 in estados:
        for s2 in estados:
            if tabela_minimiza[(s1,s2)] == True:
                print(f"S1: {s1}")
                print(f"S2: {s2}")
                if s1 in estados_finais and s2 in estados_finais and (s1 not in n_finais and s2 not in n_finais): #verifica onde ta vazio  e se é final e dps junta
                    n_finais.extend([s1,s2])
                    n_finais = list(set(n_finais)) #se tiver repetido tira.
                    if (n_finais == s1 and n_finais == s2):
                        novos_estados_finais = estados_finais
                    else:
                        novos_estados_finais = [''.join(n_finais)]
                        #print(estados_finais)
    
    # Gerando novo delta_afd
    for (estado, simbolo), destinos in delta_afd.items():
        if destinos:
            novo_estado = combina_estados.get(estado, estado)
            novo_destino = combina_estados.get(destinos[0], destinos[0])
            novo_delta_afd[(novo_estado, simbolo)] = novo_destino
            
    
    print(f"Novos estados: {novos_estados}")

    print(f"Novos estados finais: {n_finais} e {novos_estados_finais}")

    novo_estado_inicial = combina_estados.get(estado_ini, estado_ini)
    
    # Criar o gráfico do autômato minimizado
    automato = Digraph()
    automato.attr(rankdir='LR')
    automato.attr('node', shape='circle')
    
    automato.node('', shape='none')
    automato.edge('', novo_estado_inicial)
    
    for estado in n_finais:
        """
        if estado in n_finais:
            estado = novos_estados_finais
        """
        automato.node((estado), shape='doublecircle', fontsize='19', fontcolor='green')
    
    for (estado, simbolo), destino in novo_delta_afd.items():
        """
        if destino in n_finais:
            destino = novos_estados_finais
        """
        automato.edge(estado, (destino), label=simbolo)

    automato.render(pasta_afd + 'AutomatoMinimizado', format='png', cleanup=True)


    #Equivalencia
    aux_alfa = alfabeto.split()
    print("Deseja testar equivalência do AFN e AFD convertido? S/s-SIM | N/n-NÃO")
    res = input()
    if res == 'S' or res == 's':
        print("Digite o tamanho do teste: (Min = 1 Max = ATÉ ONDE CONSEGUIR)\n")
        tam_equivalencia = int(input())
        cont = cont2 = cont3 = cont4 = 0
        
        novo_delta_afd = {key: [value] for key, value in novo_delta_afd.items()}
        for _ in range(tam_equivalencia):
            
            entrada = base.gerarEntradaAleatoria(aux_alfa)
            print(entrada)
            estados_atuais = [novo_estado_inicial]
            for simbolo in entrada:
                    print("Minimizado\n")
                    print(f"Estados atuais: {estados_atuais}")
                    novos_estados_1 = []
                
                    for estado_atual in estados_atuais:
                        prox_estados = novo_delta_afd.get((estado_atual, simbolo), [])
                        novos_estados_1.extend(prox_estados)
                    
                    estados_atuais = novos_estados_1
                
            print(f"Entrada atual: {simbolo}")
            print(f"Próximos estados: {estados_atuais}")
            
            if any(estado in n_finais for estado in estados_atuais):
                cont = cont + 1
                print("Reconheceu!")
            else:
                cont2 = cont2 - 1
                print("Não reconheceu!")
            
            print("/-----------------------------------------------------/")
            estados_atuais2 = [estado_ini]

            for simbolo in entrada:
                    print("Nao minimizado")
                    print(f"Estados atuais: {estados_atuais2}")
                    novos_estados2 = []
                
                    for estado_atual2 in estados_atuais2:
                        prox_estados2 = delta_afd.get((estado_atual2, simbolo), [])
                        novos_estados2.extend(prox_estados2)
                    
                    estados_atuais2 = novos_estados2
                
            print(f"Entrada atual: {simbolo}")
            print(f"Próximos estados: {estados_atuais2}")
            
            if any(estado in estados_finais for estado in estados_atuais2):
                cont3 = cont3 + 1
                print("Reconheceu!")
            else:
                cont4 = cont4 - 1
                print("Não reconheceu!")
        if cont == cont3 and cont2 == cont4:
            print("\nSão equivalentes\n")
        else:
            print("\nNão são")