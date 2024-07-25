import base
import os

def converte_afn_afd():
    pasta_afn = "AFNs/"
    pasta_afd = "AFDs/"

    # Carrega a tabela de transições do AFN
    delta_afn = base.converte_txt_dict(pasta_afn)

    estado_inicial = None
    estados_finais = set()
    alfabeto = set()

    # Carrega os estados finais, alfabeto e estado inicial do AFN
    estados_finais, alfabeto, estado_inicial = base.push_ini_fini_alfabeto(pasta_afn, estado_inicial, estados_finais, alfabeto)
    
    # Obtém os estados do AFN
    #estados = base.retorna_estados(pasta_afn)
    
    # Inicializa o estado inicial do AFD
    estados_afd = set()  # Conjunto de estados do AFD
    tabela_transicoes_afd = {}  # Dicionário para armazenar a tabela de transições
    estados_finais_afd = set()

    # Inicializa a fila de estados a serem processados 
    fila = [frozenset([estado_inicial])]

    while fila:
        estados_atual = fila.pop(0)
        estados_afd.add(estados_atual)

        for simbolo in alfabeto:
            # Conjunto de estados para o próximo estado AFD
            proximo_estado = set()

            for estado in estados_atual:
                if estado in delta_afn and simbolo in delta_afn[estado]:
                    proximo_estado.update(delta_afn[estado][simbolo])

            if proximo_estado:
                proximo_estado_frozen = frozenset(proximo_estado)
                if proximo_estado_frozen not in estados_afd:
                    fila.append(proximo_estado_frozen)
                tabela_transicoes_afd[(estados_atual, simbolo)] = proximo_estado_frozen

        # Verifica se o estado atual é um estado final do AFD
        if any(estado in estados_finais for estado in estados_atual):
            estados_finais_afd.add(estados_atual)

    # Salva o AFD em um arquivo 
    print(tabela_transicoes_afd)
    base.armazena_arquivo(pasta_afd, tabela_transicoes_afd)

    
