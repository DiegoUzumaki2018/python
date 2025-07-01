a=[0,0,0,0]
soma=int(0)
contpar=int(0)
cont=int(0)
for cont in range(0,4,1):
        a[cont]=int(input("Digite um numero"))
        if(a[cont]%2==0):
                soma=soma+a[cont]
                contpar=contpar+1
print(f"a soma é {soma} é a quantidade é {contpar}")