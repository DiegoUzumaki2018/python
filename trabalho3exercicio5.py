numero=[0,0,0]
somapar=int(0)
somaimpar=int(0)
for cont in range(3):
        numero[cont]=int(input("Digite um numero"))
        if(numero[cont]%2==1):
                somaimpar=somaimpar+numero[cont]
        if(numero[cont]%2==0):
                somapar=somapar+numero[cont]
print(f"a soma dos pares é {somapar} e a soma dos numeros impares é {somaimpar}")