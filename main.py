import create
import converte
import minimiza
print('Bem vindo ao Sistema de AFNS e AFDS')


while 1:
    print("Menu de opções",end="\n")
    print(" 1. Criar e Testar",end="\n")
    print(" 2. Converter um AFN -> AFD",end="\n")
    print(" 3. Minimizar um AFD", end="\n")
    print(" 4. Sair",end="\n")
    op = int(input("Entre com a opção desejada: "))
    if op == 1:
        create.create_afnafd()
        continue
    elif op == 2:
        converte.converte_afnafd()
        continue
    elif op == 3:
        minimiza.minimiza_afd()
        continue
    elif op == 4:
        print("Fechando... Adeus =D",end="\n")
        break
