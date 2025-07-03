salario=[0,0,0,0]
maior=int(0)
for cont in range(4):
    salario[cont]=int(input("Qual é o seu salario"))
    if(salario[cont]>maior):
        maior=salario[cont]

print(f"o maior salario é {maior}")