def converte_afnafd():
    import os
    import base
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
    pasta_afd = "AFDs/"
    estado_ini = ""
    estados_finais = []
    delta_afn = base.converte_txt_dict(pasta_afn)
    estado_ini, estados_finais = base.push_ini_fini(pasta_afn,estado_ini,estados_finais)
    
    
