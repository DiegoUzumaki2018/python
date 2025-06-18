cont=int(0)
contnum1=int(0)
contnum2=int(0)
while (cont!=5):
        cont=cont+1
        nume=int(input("Digite um numero"))
        if(nume%9==0):
                contnum1=contnum1+1
        if(nume%7==0):
                contnum2=contnum2+1

print(f"foram indetificados{contnum1} numeros que são multiplos de 9 e {contnum2} numeros que são multiplo por 7")