cont=int(0)
soma=int(0)
media=int(0)
for cont in range(0,3,1):
            valor1=float(input("Qual é o valor?"))
            valor2=float(input("Qual é o valor?"))
            valor3=float(input("Qual é o valor?"))
            soma=valor1+valor2+valor3
            media=soma/3
            if(soma>media*2):
                    print("verdadeiro")
            if(soma<media*2):
                    print("falso")
