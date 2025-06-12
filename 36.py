numero1=int(input("Qual numero"))
numero2=int(input("Qual é o numero"))
numero3=int(input("Qual é o numero"))
numero4=int(input("Qual é o numero"))
maior=int(0)
somapar=int(0)
contpar=int(0)
if(numero1%2==0):
  somapar=somapar+numero1
if(numero2%2==0):
  somapar=somapar+numero2
if(numero1%2==0):
  somapar=somapar+numero3
if(numero1%2==0):
  somapar=somapar+numero4


if(numero1%2==0):
  contpar=contpar+1
if(numero2%2==0):
    contpar=contpar+1
if(numero3%2==0):
   contpar=contpar+1
if(numero4%2==0):
    contpar=contpar+1


if(numero1%2==0 and numero1>maior):
    maior=numero1
if(numero2%2==0 and numero2>maior):
   maior=numero2
if(numero3%2==0 and numero3>maior):
    maior=numero3
if(numero4%2==0 and numero4>maior):
   maior=numero4


print("O total de pares"+ str(contpar) + " a soma dos pares " + str(somapar) +"é maior par " + str(maior))