"""
Composta por uma fita que vai ter uma string.
estado inicial
estados_correntes
estados_finais
função de transição do tipo
dicionario
"""
from basemt import MaquinaTuring
import basemt
simbolo_vazio = " "
fita = {} #dict de fitas.
estado_inicial = ""
estados_finais = None
estados_correntes = None
regras_transicao = None
entrada_fita = ""

def maquina_turing():
    """
    print("Entrada: \n")
    entrada_fita = input()
    print("Estado inicial: \n")
    estado_inicial = input()
    print("Estados finais: \n")
    estados_finais = input().split()

    print("Digite as regras de transição: ")
    for estado in estados_correntes:
    """
    
    print("Entrada: \n")
    entrada_fita = input()
    print("Estado inicial: \n")
    estado_inicial = input()
    print("Estados finais: \n")
    estados_finais = input().split()

    print("Agora será a hora de digitar")

    regras_transicao = {("q0","a"):("q0", "b", "R"),
                       ("q0","b"):("q0", "a", "R"),
                       ("q0","c"):("q1", "b", "R"),
                       ("q1", "c"):("q0", "a", "R"),
                       ("q0"," "):("q2"," ", "N")}

    objMt = MaquinaTuring(entrada_fita, simbolo_vazio=simbolo_vazio, estado_inicial=estado_inicial, 
    estados_finais=estados_finais, regras_transicao=regras_transicao)

    print("Entrada na fita: \n" + objMt.retorna_fita())
    while 1: ##Imitar um PC.
        try:
            if not objMt.eh_final():
                objMt.maquina_atualizando()
            else:
                break
        except ValueError:
            print("TELAA AZULLLL \n")
    
    print("Operação realizada com sucesso, abaixo está a saída.\n")
    print("Resultado da fita: \n" + objMt.retorna_fita())

    print("O tamanho da fita de entrada foi: ", basemt.tamanho_fita(entrada_fita))





