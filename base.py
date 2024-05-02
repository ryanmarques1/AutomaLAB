from graphviz import Digraph

def desenhar_automato(estado_inicial, estados_finais, delta):
    automato = Digraph() #Definindo que a var automato é do tipo Digraph()
    automato.attr(rankdir='LR') #LR siginifica da esquerda para direita. entao o automato será criado usando essa regra
    automato.attr('node', shape='circle') #definindo os atributos do node (nós)
    
    automato.node(estado_inicial, shape='circle', fontsize='19', fontcolor='black') #edefinindo o nó inicial estado inicial receber circulo
    for estado_final in estados_finais: 
        automato.node(estado_final, shape='doublecircle', fontsize='19', fontcolor='green')#colocando circulo duplo em todos os estados finais.
    for estado_origem, simbolo, estado_destino in delta:
        automato.edge(estado_origem,estado_destino,label=simbolo) #edge insere as setas de acordo com o delta, label = simbolo siginica que em cima da seta estará o simbolo.
    return automato

def armazena_arquivo(pasta, delta):
    arqAUTOMATO = open(pasta + ('automatoCriado.txt'), 'w') #teste
    arqAUTOMATO.writelines(str(delta))
    return arqAUTOMATO

def dict_lista(dict):
    lista = [(estado_origem, simbolo, estado_destino) for (estado_origem, simbolo), estados_destinos in dict.items() for estado_destino in estados_destinos]
    return lista

