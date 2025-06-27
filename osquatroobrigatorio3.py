cont=int(0)
cont2=int(0)
soma=int(0)
for cont in range(999):
        produto=int(input("Qual é o valor do produto?"))
        quer=str(input("Quer continuar?"))
        if(quer=="n"):
             soma=soma+produto
             cont2=cont+1
             break
print(" a soma dos valores dos produtos é " + str(soma) + "\n" + " é a quantidade de itens é " + str(cont2))   