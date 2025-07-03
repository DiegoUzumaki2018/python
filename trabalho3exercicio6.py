numero=[0,0,0,0]
contpar=int(0)
somapar=int(0)
maior=int(0)
for cont in range(3):
        numero[cont]=int(input("Digite um numero"))
        if(numero[cont]%2==0):
                somapar=somapar+numero[cont]
                maior=numero[cont]
                contpar=contpar+1
print(f"foram digitados {contpar} numeros pares A soma desses pares é {somapar} O maior numero par é {maior}")