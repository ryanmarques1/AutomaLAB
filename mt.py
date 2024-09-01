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
simbolo_vazio = ' '
estado_inicial = ""
estados_finais = None
estados_correntes = None
regras_transicao = None
entrada_fita = ""

regras_transicao = {}
estado_atual = ""
simbolo_atual = ""
estado_novo = ""
simbolo_novo = ""
movimento_cabeca = ""

def maquina_turing():
    """
    regras_transicao = {('q0',' '): ('qaccept',' ', 'R'),
                        ('q0','('): ('q1', 'X', 'R'),
                        ('q0', ')'): ('qreject', ')', 'R'),
                        ('q0', 'X'): ('q0', 'X', 'R'),

                        ('q1', ')'): ('q2', 'X', 'L'),
                        ('q1', '('): ('q1', '(', 'R'),
                        ('q1', 'X'): ('q1', 'X', 'R'),
                        ('q1', ' '): ('qreject', ' ', 'R'),

                        ('q2', 'X'): ('q2', 'X', 'L'),
                        ('q2', '('): ('q0', '(', 'R'),
                        ('q2', ' '): ('q3', ' ', 'R'),

                        ('q3', 'X'): ('q3', 'X', 'R'),
                        ('q3', ' '): ('qaccept', ' ', 'R'),
                        ('q3', '('): ('qreject','(', 'R'),
                        ('q3', ')'): ('qreject', ')', 'R'),

                        ('q4', 'X'): ('q4', 'X', 'R'),
                        ('q4', ' '): ('qaccept',' ', 'R'),}
    """
    
    
    print("Entrada: \n")
    entrada_fita = input()
    print("Estado inicial: \n")
    estado_inicial = input()
    print("Estados finais: \n")
    estados_finais = input().split()
    

    print("Agora será a hora de digitar as regras de transição da máquina:")
    print("Seguindo desta forma: [chave] estado, simbolo -> [valor] estado_destino, simbolo_novo, movimento_cabeça")
    print("Para simbolizar uma transição  -> (' ') vazia dê espaço e aperte enter")
    
   
    print("Digite a quantidade de regras: ")
    tam_regras = int(input())
    for i in range(tam_regras):
        estado_atual = input("Entre com o estado atual: ")
        simbolo_atual = input("Entre com o simbolo atual: ")
        estado_novo = input("Entre com o estado novo: ")
        simbolo_novo = input("Entre com o simbolo novo: ")
        movimento_cabeca = input("Entre com a direção da cabeça: ")
        chave = (estado_atual, simbolo_atual)
        valor = (estado_novo, simbolo_novo, movimento_cabeca)
        regras_transicao.update({chave: valor})
    
    

    objMt = MaquinaTuring(entrada_fita, simbolo_vazio=simbolo_vazio, estado_inicial=estado_inicial, 
    estados_finais=estados_finais, regras_transicao=regras_transicao)

    print("Entrada na fita: \n" + objMt.retorna_fita())
    while not objMt.eh_final(): ##Imitar um PC.
        try:
            objMt.maquina_atualizando()
        except ValueError:
            print("Error \n")

    print("Operação realizada com sucesso, abaixo está a saída.\n")
    print("Resultado da fita: \n" + objMt.retorna_fita())

    print("O tamanho da fita de entrada foi: ", basemt.tamanho_fita(entrada_fita))


#Verificação de parentese balanceado

"""
('q0',' '): ('qaccept',' ', 'R')
('q0','('): ('q1', 'X', 'R')
('q0', ')'): ('qreject', ')', 'R')
('q0', 'X'): ('q0', 'X', 'R')

('q1', ')'): (''q2'', 'X', 'L')
('q1', '('): ('q1', '(', 'R')
('q1', 'X'): ('q1', 'X', 'R')
('q1', ' '): ('qreject', ' ', R)

('q2', 'X'): ('q2', 'X', 'L')
('q2', '('): (q0, '(', 'R')
('q2', ' '): ('q3', ' ', 'R')

('q3', 'X'): ('q3', 'X', 'R')
('q3', ' '): ('qaccept', ' ', 'R')
('q3', '('): ('qreject','(', 'R')
('q3', ')'): ('qreject', ')', 'R')

('q4', 'X'): ('q4', 'X', 'R')
('q4', ' '): ('qaccept',' ', 'R')

----------------------------------------------


"""



