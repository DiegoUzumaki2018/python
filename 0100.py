par=[0,0,0,0]
somapar=int(0)
contimpar=int(0)
contpar=int(0)
cont=int(0)
impar=[0,0,0,0]
somaimpar=int(0)
for cont in range(0,4,1):
        
        par[cont]=int(input("Digite um valor"))
        if(par[cont]%2==0):
                somapar=somapar+par[cont]
                contpar=contpar+1
        

print(f"a soma dos pares é {somapar} \n e a quantidade de pares{contpar}")

for cont in range(0,4,1):
            impar[cont]=int(input("Digite um numero"))
            if(impar[cont]%2==1):
                contimpar=contimpar+1
                somaimpar=somaimpar+impar[cont]
print(f"a soma dos pares é {somaimpar} \n e a quantidade de impares{contimpar}")