import create
import converte
import minimiza
import base
#Variaveis para controle de acesso indeterminado
caracteres_especiais = "!@#$%&*()-+=<>:;^~.,][}{?/"
#Variaveis para controle de acesso indeterminado

print('Bem vindo ao Sistema AUTOLAB', end="\n")

print("\nVerificando a existência de um AFN e ou AFD criado...\n")

base.verifica_existencia()

afn = None

while 1:
 
    
    print("Menu Principal",end="\n")
    print(" 1. Criar e Testar",end="\n")
    print(" 2. Converter um AFN -> AFD",end="\n")
    print(" 3. Minimizar um AFD", end="\n")
    print(" 4. Sair",end="\n")
    op = int(input("Entre com a opção desejada: "))
    if op == 1:
        create.create_afnafd(caracteres_especiais)
        continue
    elif op == 2:
        converte.afn_para_afd()
        continue
    elif op == 3:
        minimiza.minimiza_afd()
        continue
    elif op == 4:
        print("Fechando... Adeus =D",end="\n")
        break
