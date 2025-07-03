idade=int(input("Digite sua idade"))
salario=float(input("digite seu salario"))

print("sua idade é" + str(idade) + "anos e seu salario é" + str(salario))
print(f"sua idade é {idade} anos e seu salario é {salario}")

contador=int(0)
while (contador!=3):
    contador=contador+1
    salario=int(input("digite seu salario"))
    if(salario==2000):
        break