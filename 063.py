contador=int(0)
contador2=int(0)
contador3=int(0)
while (contador!=7):
        contador=contador+1
        numero=int(input("digite o numero"))
        if(numero%5==0):
                contador2=contador2+1
        if(numero%3==0):
                contador3=contador3+1
print(f"foram identificados {contador2} numeros que são multiplos de cinco e {contador3} numeros que são multiplo por três") 