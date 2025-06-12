compra1=int(input(" Qual é o valor da primeira compra? "))
compra2=int(input(" Qual é o valor da segunda compra? "))
compra3=int(input(" Qual é o valor da terceira compra? "))
soma=int(compra1+compra2+compra3)
media=int(soma/3)
if(soma>media*2):
    print("verdadeiro")
if(soma<media*2):
    print("falso")