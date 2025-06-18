cont=int(0)
contpar=int(0)
contimpar=int(0)
for cont in range (0,3,1):
            valores=int(input("Qual é o valor"))
            if(valores%2==0):
                    contpar=contpar+1
            if(valores%2==1):
                    contimpar=contimpar+1

print(f"foram encontrados {contpar} números pares e {contimpar} numeros impares")
