import p0110funcoes
a=int(input("Qual é o valor?"))
b=int(input("Digite outro valor"))
c=str(input("Qual dessas operações?"))

if(c=="Soma"):
    p0110funcoes.soma(a,b)
if(c=="subtrair"):
    p0110funcoes.diminuir(a,b)
if(c=="multiplicar"):
    p0110funcoes.mult(a,b)
if(c=="divisão"):
    p0110funcoes.divi(a,b)