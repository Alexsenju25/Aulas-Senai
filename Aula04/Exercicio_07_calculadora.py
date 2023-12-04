numero_1 = float (input  ("Digite o primeiro número: )"))
numero_2 = float (input ( "Digite o segundo número: )"))

while (True):

    print("Escolha uma opção \n")
    print("Opção 1: Adição \n")
    print("Opção 2: Subtração \n")
    print("Opção 3: Multiplicação \n")
    print("Opção 4: Divisão \n")
    print("Opção 5: Sair \n")

    opcao = int(input("Escolha uma opção"))

    if(opcao == 5):
        break
    elif opcao == 1:
        print(f"A soma do {numero_1} com o {numero_2} é:  ", numero_1 + numero_2)
