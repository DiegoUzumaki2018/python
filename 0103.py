import random
a=int(0)
b=int(0)
soma=int(0)
cont=int(0)
v=[0,0,0,0]
a=v[random.randint(0,2)]
b=int(input("Digite o numero da cor"))
c=int(input("Qual é seu valor?"))
if(b==a and b==1):
    c=c*2
    print(c)
if(b==a and b==2):
    soma=c*2
    print(c)
if(b==a and b==3):
     soma=c*14
     print(c)
if(b!=a):
   soma=soma-c
   print("perdeu")

