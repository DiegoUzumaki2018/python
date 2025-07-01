import p0128funcoes as fn
import random
a=[1,2,3,4]
soma=float(0)
for cont in range(4):
    a[cont]=random.randint(1,4)
    b=int(input("Digite um numero de 1 a 4")) 
    t = int(fn.analisar(a[2]))
    y = int(fn.analisar2(a[1]))
    soma=(t+y)*3.14
    print(soma)
