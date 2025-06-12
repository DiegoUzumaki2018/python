valor1=int(input(" Digite um valor "))
valor2=int(input(" digite outro valor "))
valor3=int(input(" digite mais outro valor "))
contadorimpar=int(0)
contadorpar=int(0)
if( valor1 %2 == 0 ):  
    contadorpar=contadorpar+1
if(valor2 %2==0):
    contadorpar=contadorpar+1
if(valor3 %2==0):
    contadorpar=contadorpar+1
if( valor1 %2 == 1 ):
    contadorimpar=contadorimpar+1
if(valor2 %2==1):
    contadorimpar=contadorimpar+1
if( valor3 %2==1):
   contadorimpar=contadorimpar+1
print(" foram encontrandos " + str(contadorpar) + " numeros pares e " + str(contadorimpar) + " numeros impares ")