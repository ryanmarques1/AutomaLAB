from turing_machine import Turing_Machine
import string
import sys

def checar_palindromo(string_inicial):
    # Definir conjunto de caracteres permitidos (letras minúsculas e espaço)
    lista_de_caracteres = list(string.ascii_lowercase)
    lista_de_caracteres.append(' ')  # Permitir espaços
    
    # String inicial
    print('Verificando... ' + string_inicial)
    print('---')
    lista_inicial = list(string_inicial)
    
    # Verificar se todos os caracteres são permitidos
    for i in lista_inicial:
        if i not in lista_de_caracteres:
            print(f'Erro. O caracter inicial "{i}" não está na lista de caracteres permitidos')
            sys.exit()
            
    # Anexar marcador de fim de lista
    lista_inicial.append(0)
    
    # Configurar a máquina de Turing
    i_cabeca_escrita = 0
    i_estado = 'q1'
    i_lista_caracteres = lista_inicial
    
    # Iniciar a máquina de Turing
    maquina = Turing_Machine(i_estado, i_cabeca_escrita, i_lista_caracteres)
    print(maquina.obter_estado(), maquina.cabeca(), maquina.lista())
    
    # Executar a máquina
    passos = 0
    while maquina.obter_estado() != 'qy' and maquina.obter_estado() != 'qn' and passos < 1000:
        maquina.maquina_de_atualizacao(lista_de_caracteres)
        print(maquina.obter_estado(), maquina.cabeca(), maquina.lista())
        passos += 1

    # Remover o marcador de fim de lista (0)
    lista_final = [x for x in maquina.lista() if x != 0]
    
    print('----')
    
    if maquina.obter_estado() == 'qy':
        print(f'"{string_inicial}" é um palíndromo! Passos: {passos}')
    else:
        print(f'"{string_inicial}" NÃO é um palíndromo! Passos: {passos}')

entrada = input().strip()
checar_palindromo(entrada)
