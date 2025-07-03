a=[0,0,0,0,0,0]
maior=int(0)
menor=int(99999)
media=int(6)
soma=int(0)
cont=int(0)
for cont in range(0,6,1):
    a[cont]=int(input("Digite uma nota"))
    soma=soma+a[cont]
    media=soma/a[cont]
    if(a[cont]>maior):
        maior=maior
    if(a[cont<menor]):
        menor=menor
    
print(f"a maior nota é {maior} e a menor nota é {menor} e a media é {media}")

   