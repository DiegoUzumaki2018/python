cont=int(0)
contpar=int(0)
somapar=int(0)
maiorpar=int(0)
for cont in range(0,4,1):
            numero=int(input("Digite um numero"))
            if(numero%2==0):
                    maiorpar=numero
                    somapar=somapar+numero
                    contpar=cont+1
print(f"foram digitado{contpar} a soma desses números pares é {somapar} o maior numero par é {maiorpar}")