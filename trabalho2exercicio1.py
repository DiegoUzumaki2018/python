cont=int(0)
somaimpar=int(0)
somapar=int(0)
while(cont !=3):
        cont=cont+1
        numero=int(input("Digite um numero"))
        if(numero%2==0):
                somapar=somapar+numero
        if(numero%2==1):
                somaimpar=somaimpar+numero
print(f"a soma dos impares é {somaimpar} e a soma dos pares é {somapar}")