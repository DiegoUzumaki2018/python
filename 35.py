numero1=int(input("Qual é seu numero"))
numero2=int(input("Qual é seu numero"))
numero3=int(input("Qual é seu numero"))
somapar=int(0)
somaimpar=int(0)

if(numero1%2==0):
    somapar=somapar+numero1
if(numero2%2==0):
    somapar=somapar+numero2
if(numero3%2==0):
    somapar=somapar+numero3
if(numero1%2==1):
    somaimpar=somaimpar+numero1
if( numero2%2==1 ):
    somaimpar=somaimpar+numero2
if( numero3%2==1):
    somaimpar=somaimpar+numero3

print("a soma dos pares é " + str(somapar) + " a soma dos impares é " + str(somaimpar))