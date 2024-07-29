import base

from graphviz import Digraph
def converte_afn_afd():
    pasta_afn = "AFNs/"
    pasta_afd = "AFDs/"

    res = base.verifica_existencia(pasta_afn)
    estado_inicial = None
    estados_finais = set()
    alfabeto = set()
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

    # Salva o AFD em um arquivo 
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
