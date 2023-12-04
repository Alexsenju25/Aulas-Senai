idade = int (input("Digite a sua idade para saber se deve votar :"))

if (idade < 16 ):
    print ("Você não pode votar. ")
elif (idade > 16 and idade < 18 ):
    print ( "Seu voto é facultativo. ")
elif (idade > 18 and idade < 66 ):
    print ("Seu voto é obrigatório. ")

else:
    print ("Seu voto é facultativo")

