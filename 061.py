somapar=int(0)
somaimpar=int(0)

contador=int(0)
while (contador != 5):
        contador=contador+1
        numero=int(input("Digite 5 numeros"))
        if(numero%2==0):
                somapar=somapar+numero
        if(numero%2==1):
                somaimpar=somaimpar+numero
print(f"a soma dos impares {somaimpar} e a soma dos pares {somapar}")
