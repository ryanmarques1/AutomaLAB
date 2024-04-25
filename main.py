import create
print('Bem vindo ao Sistema de AFNS e AFDS')

while 1:
    print(" 1. Criar e Testar "
      " 2. Converter um AFN -> AFD "
      " 3. Minimizar um AFD "
      " 4. Sair ")
    
    print("",end="\n")
    op = int(input("Entre com a opção desejada: "))
    if op == 1:
        create.create_afnafd()
        continue
    elif op == 2:
        continue
    elif op == 3:
        continue
    elif op == 4:
        break
