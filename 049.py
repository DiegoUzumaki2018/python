n1=int(input("Digite numero"))
n2=int(input("Digite numero"))
n3=int(input("Digite numero"))
maior=int(0)
menor=int(0)
medio=int(0)
igual=int(0)
if(n1>n2 and n1>n3 and n2>n3):
    maior=n1
    medio=n2
    menor=n3
if(n1>n2 and n1>n3 and n3>n2):
    maior=n1
    medio=n3
    menor=n2
if(n2>n1 and n2>n3 and n1>n3):
    maior=n2
    medio=n1
    menor=n3
if(n2>n1 and n2>n3 and n3>n1):
    maior=n2
    medio=n3
    menor=n1
if(n3>n1 and n3>n2 and n1>n2):
    maior=n3
    medio=n1
    menor=n2
if(n3>n1 and n3>n2 and n2>n1):
    maior=n3
    medio=n2
    menor=n1
if(n1 == n2 and n2==n3 and n3==n1):
    print("os numeros são iguais")

print(str(maior)+str(medio)+str(menor))