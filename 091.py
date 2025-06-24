cont=int(0)
soma=int(0)

numero=int(input("Digite um numero "))
numero2=int(input("Digite um numero "))
for cont in range(0,200,1):
            soma=numero+numero2
            if(soma>=1000):
                soma=soma-1000
                break

print(soma)           