cont=int(0)
cont2=int(0)
soma=int(0)
for cont in range(1,7,1):
            valor=int(input("Digite valor"))
            if(valor%2==0):
                    soma=soma+valor
                    cont2=cont
print("Foram digitado\n" + str(cont2) + " e a soma é " + str(soma))