valor=[0,0,0]
soma=int(0)
média=int(0)
for cont in range(3):
        valor[cont]=int(input("Qual é o valor?"))
        valor[cont]=int(input("Qual é o valor?"))
        valor[cont]=int(input("Qual é o valor?"))
        soma=soma+valor[cont]
        média=soma/3
        if(soma>média*2):
                print("verdadeiro")
        if(soma<média*2):
                print("falso")
