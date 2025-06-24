cont=int(0)
tentativas=int(0)
while(cont!=9999999):
    cont=cont+1
    nome=str(input("Qual seu nome?"))
    idade=int(input("Qual é a sua idade?"))
    if(nome=="João" and idade>35):
                 print("ok")
                 break
    if(cont==3):
           print("bloqueado")
           break

    else:
     print("repita novamente")
                