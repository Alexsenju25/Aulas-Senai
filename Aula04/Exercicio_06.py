import random
numero_sorteado = random.randint(1,100)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número (entre 1 e 100)"))
    tentativas += 1

    if tentativa == numero_aleatorio:
        print (f"Parabéns! Você acertou em {tentativa} tentativas. ")
        break
    elif tentativa < numero_aleatorio:
        print("Tente um número maior. ")
    else:
        print ("Tente um número menor. ")