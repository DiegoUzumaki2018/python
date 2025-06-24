cont=int(0)
cont2=int(0)
while(cont!=99999):
            cont=cont+1
            numero=int(input("Digite um numero"))
            quer=str(input("Quer continuar?"))
            if(quer=="n"):
                    break
            if(numero%2==1):
                    cont2=cont2+1
                   
                    
print("numero de primos é " + str(cont2))

                    
