def minimiza_afd():
    import os
    import base
    from tabulate import tabulate
    print("Minimiza AFD", end="\n")
    pasta_afd = "AFDs/"
    estado_ini = ""
    estados_finais = []
    alfabeto = []
    delta_afd = base.converte_txt_dict(pasta_afd)
    
    estados = base.retorna_estados(pasta_afd)
    estado_ini, estados_finais, alfabeto = base.push_ini_fini_alfabeto(pasta_afd, estado_ini, estados_finais, alfabeto)
    
    matriz_tabela  = [[''] + estados]
    for i in estados:
        linha = [i]
        print([i])
        for j in estados:
            if i == j:
                linha.append('X')
            else:
                linha.append('')
        matriz_tabela.append(linha)

    for i in range(1, len(estados) + 1):
        for j in range(i):
            matriz_tabela[i][j + 1] = 'X'
            
                
    print(estados)
    print(tabulate(matriz_tabela, headers='firstrow', tablefmt='fancy_grid'))
    #print(delta_afd)


    #Segunda Etapa = Verificação -> ESTADO FINAL X FINAL & ESTADO INICIAL COM INICIAL
    #Se acontecer a colisão de ESTADO INICIAL X FINAL, SERÁ COLOCADO UM 'X' NA TABELA

    for i in range(1, len(estados) + 1):
        for j in range(i):
            estado1 = matriz_tabela[i][0]  # Estado da linha i
            estado2 = matriz_tabela[0][j + 1]  # Estado da coluna J + 1
            if (estado1 == estado_ini and estado2 in estados_finais) or (estado2 == estado_ini and estado1 in estados_finais):
                matriz_tabela[i][j + 1] = 'X'

    print(tabulate(matriz_tabela, headers='firstrow', tablefmt='fancy_grid'))

         