cont=int(0)
somapar=int(0)
somaimpar=int(0)
for cont in range(0,3,1):
            numeros=int(input("Qual é o numero"))
            if(numeros%2==0):
                    somapar=somapar+numeros
            if(numeros%2==1):
                    somaimpar=somaimpar+numeros
print(f"a soma dos numeros pares é {somapar} e a soma dos numeros impares é {somaimpar}")