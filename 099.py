a=[0,0,0]
cont=int(0)
cont2=int(0)
for cont in range(0,3,1):
            a[cont]=int(input("Digite um numero"))
            if(a[cont]==14):
                    cont2=cont2+1
print(f"apareceu {cont2}")