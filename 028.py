velocidade=int(input(" qual é a velocidade do carro "))
if(velocidade <= 80):
    print("velocidade segura")
else:
     multa=int(450+10*velocidade)
     print(" sua multa é " + str(multa) + " reais " )