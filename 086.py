import random
cont=int(0)
cont2=int(0)
while(cont!=99999):
            cont=cont+1
            sorteio=random.randint(1,10)
            numero=int(input("digite um numero"))
            if(numero>sorteio):
                    print("você errou tente um numero maior")
            if(numero<sorteio):
                    print("você errou tente um numero menor")
            if(numero==sorteio):
                cont2=cont
                print(f"sucesso você acertou após {cont2} tentativas")
                break