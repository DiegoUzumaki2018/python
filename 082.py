cont=int(0)
quan=int(0)
quant2=int(0)
quantos=int(0)
for cont in range(0,4,1):
            idade=int(input("Qual é a sua idade?"))
            sexo=str(input("Qual é seu sexo?"))
            if(idade>10):
                    quan=quan+1
            if(sexo=="h"):
                    quantos=quantos + 1
            if(sexo=="m" and idade<20):
                    quant2=quant2 + 1
                    

print(f"a quantidade de mulheres de menor de 20 é {quant2}")
print(f"a quantidade de homens é {quantos}")
print(f"no total de pessoas que tem mais de 10 anos é {quan}")