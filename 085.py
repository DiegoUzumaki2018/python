n50=int(0)
n20=int(0)
n10=int(0)
n2=int(0)
n1=int(0)
cont=int(0)
valor=int(input("digite o valor"))
while(valor>0):
        cont=cont+1
        if(valor>=50):
                n50=n50+1
                valor=valor-50
        elif(valor>=20):
                n20=n20+1
                valor=valor-20
        elif(valor>=10):
                n10=n10+1
                valor=valor-10
        elif(valor>=2):
                n2=n2+1
                valor=valor-2
        elif(valor>=1):
                n1=n1+1
                valor=valor-1
print(f"a nota é {n50}")
print(f"a nota é {n20}")
print(f"a nota é {n10}")
print(f"a nota é {n2}")
print(f"a nota é {n1}")