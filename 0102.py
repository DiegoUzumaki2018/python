import random
a=[0,0,0,0]
b=[0,0,0,0]
soma=int(0)
cont=int(0)
for cont in range(4):
        a[cont]=random.randint(1,5)

for cont in range(0,4,1):
        b[cont]=int(input("Digite um numero 1 a 4"))
        if(a[cont]==b[cont]):
                soma=soma+a[cont]
print(f"a soma é {soma}")