from graphviz import Digraph
import os
import time
import random

def desenhar_automato(estado_inicial, estados_finais, delta):
    automato = Digraph() #Definindo que a var automato é do tipo Digraph()
    automato.attr(rankdir='LR') #LR siginifica da esquerda para direita. entao o automato será criado usando essa regra
    automato.attr('node', shape='circle') #definindo os atributos do node (nós)
    
    
    automato.node('->', shape='none', width='0', heigth='0',label='')
    automato.edge('->', estado_inicial)
    
    for estado_final in estados_finais: 
        automato.node(estado_final, shape='doublecircle', fontsize='19', fontcolor='green')#colocando circulo duplo em todos os estados finais.
    for estado_origem, simbolo, estado_destino in delta:
        automato.edge(estado_origem,estado_destino,label=simbolo) #edge insere as setas de acordo com o delta, label = simbolo siginica que em cima da seta estará o simbolo.
    return automato

def armazena_arquivo(pasta, delta, nome):
    arqAUTOMATO = open(pasta + (nome), 'w') #teste
    arqAUTOMATO.writelines(str(delta))
    return arqAUTOMATO

def armazena_informacoes(pasta, inicio, final, alfabeto):
    arqINFOautomato = open(pasta + ('info_automato'), 'w')
    arqINFOautomato.write(inicio + '\n')
    arqINFOautomato.writelines(' '.join(final))
    arqINFOautomato.write('\n')
    arqINFOautomato.writelines(' '.join(alfabeto))
    return arqINFOautomato

def dict_lista(dict):
    lista = [(estado_origem, simbolo, estado_destino) for (estado_origem, simbolo), estados_destinos in dict.items() for estado_destino in estados_destinos]
    return lista

def converte_txt_dict(pasta):
    arquivo = open(pasta + ("automatoCriado.txt"), 'r')
    arq = arquivo.read()
    delta = {}
    for i in arq:
        delta = eval(arq) #função eval pega o conteudo do arquivo , se for válido em python é adicionado na variavel delta.
    return delta

def converte_txt_list(pasta):
    arquivo = open(pasta + ("automatoCriado.txt"), 'r')
    arq = arquivo.read()
    for i in arq:
        delta = eval(arq) #função eval pega o conteudo do arquivo , se for válido em python é adicionado na variavel delta.
    delta2 = dict_lista(delta)
    return 

def push_ini_fini_alfabeto(pasta,ini,final,alfabeto):
    arq = open(pasta + ('info_automato'), 'r')
    linhas_arq = arq.readlines()
    ini = linhas_arq[0].strip()
    final = linhas_arq[1]
    alfabeto = linhas_arq[2]
    return ini,final,alfabeto

def cria_estados(pasta, estados):
    
    arq = open(pasta + ('estados.txt'), 'w+')
    arq.writelines('\n'.join(estados))
    return arq

def retorna_estados(pasta):
    arq = open(pasta + ('estados.txt'), 'r')
    estados = arq.readlines()
    estados = [item.strip() for item in estados]
    return estados

def encontrar_estadoequi(estado, combina_estados):
        while estado in combina_estados and combina_estados[estado] != estado:
            estado = combina_estados[estado]
        return estado

def verifica_existencia(pasta):
    time.sleep(1)
    path = pasta + '/automatoCriado.txt}'
    if not os.path.isfile(path):
        print('Não existe automato criado, crie um AFD ou AFN!')

def gerarEntradaAleatoria(alfabeto):
    return ''.join(random.choice(alfabeto) for _ in range(7))