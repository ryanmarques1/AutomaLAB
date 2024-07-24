def converte_afnafd():
    import os
    import base
    import sys
    print("Converte AFN -> AFD", end="\n")
    #Precisamos pegar as funções de transição do afd que ja está armazenado ou que foi criado recentemente.
    """
    Acessamos a pasta utilizando a função converte_txt_dict, pegamos o .txt do automato e passa para o dicionario delta
    depois temos que registrar o estado_ini e estado_finais deste automato
    utilizando o arquivo info_automato acessamos ele, onde nele ja está pré-registrado
        1º Linha -> Estado Inicial
        2º Linha -> Estados Finais
    e utilizando a função push_ini_fini, pegamos o estado inicial e final do automato.
    """
    pasta_afn = "AFNs/"
    estado_ini = ""
    estados_finais = []
    alfabeto = []
    estados_afd = {estado_ini}
    delta_afd = {}

    delta_afn = base.converte_txt_dict(pasta_afn)
    delta_afn = base.dict_lista(delta_afn)
    estado_ini, estados_finais, alfabeto = base.push_ini_fini_alfabeto(pasta_afn,estado_ini,estados_finais,alfabeto)

    print(delta_afn)
    chaves_afn = {ind1[0] for ind1 in delta_afn}
    chaves_afn = list(chaves_afn)
    print(chaves_afn)
    for i in chaves_afn:
        novo_estado = ''.join(chaves_afn)
        estados = chaves_afn + [novo_estado,' ']

    print(estados)