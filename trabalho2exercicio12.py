cont=int(0)
maior=int(0)
for cont in range (0,4,1):
            salario=int(input("Qual é seu salario?"))
            if(salario>maior):
                    maior=salario
print(f"o maior salario entre as pessoas citadas é {maior}")