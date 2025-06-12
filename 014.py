preso=int(input("Qual é o preço do produto"))
des=float(input(" Qual é o desconto do produto? "))
des=(des/100)

des2=float(preso*des)
custando=float(preso-des2)

print("O produto custava " + str(preso) + " mas teve desconto de " +str (des2) + " por isso agora está custando " + str (custando) + " reais " )