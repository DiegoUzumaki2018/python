cont=int(0)
for cont in range(0,3,1):
        idade=int(input("Qual é a sua idade?"))
        nacionalidade=str(input("Qual é a sua nacionalidade?"))
        sexo=str(input("Qual é seu sexo?"))
        if(idade==18 and nacionalidade=="brasileiro" and sexo=="masculino"):
                print("Apto")
        else:
                print("não apto")