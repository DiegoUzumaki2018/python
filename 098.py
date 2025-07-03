a=[0,0,0,0]
cont=int(0)
cont2=int(0)
for cont in range(0,4,1):
        a[cont]=int(input("Digite um numero"))
        if(a[cont]==9):
                cont2=cont2+1
print(f"a apareceu {cont2}")