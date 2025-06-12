preso=int(input("Qual é preço do produto?"))
epoca=str(input("Qual é a epoca do ano?"))
if(epoca=="Carnaval"):
    preso=preso + (preso*0.10)
if(epoca=="Ferias escolares"):
    preso=preso + (preso*0.20)
if(epoca=="Dia das Crianças"):
    preso=preso + (preso*0.5)
if(epoca=="Black Friday"):
    preso=preso + (preso*0.30)
if(epoca=="Natal"):
    preso=preso + (preso*0.5)

print("o preço final em cada caso é" + str(preso))
