velocidade=int(input(" qual é a velocidade? "))
excesso=velocidade-80
if(excesso>=0 and excesso <=20):
    multa1=int(150+5+velocidade)
    print("limite de velocidade excedido. Sua multa é " + str(multa1) + "reais")
if(excesso>=21 and excesso<=80):
    multa2=int(250+10+velocidade)
    print("limite de velocidade excedido.Sua multa é " + str(multa2) + "reais")
if(excesso>=81 and excesso<=200):
    multa3=int(500+20+velocidade)
    print("limite de velocidade excedido.Sua multa é " + str(multa3) +"reais")
if(excesso>200):
    print("veiculo será confiscado")