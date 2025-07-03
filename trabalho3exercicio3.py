valores=[0,0,0]
impares=int(0)
pares=int(0)
for cont in range(3):
    valores[cont]=int(input("Digite um valor"))
    if(valores[cont]%2==0):
        pares=pares+1
    if(valores[cont]%2==1):
        impares=impares+1
print(f"foram encontrados {pares} numeros pares e {impares} números impares")
