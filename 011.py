peso=int(input("Qual é seu peso? "))
sanduiches=int(input("Quantos sanduiches vc comeu? "))
preso=float(8.50)
grama=int(sanduiches*100)
novo=int(peso+grama)
valor=float(sanduiches+8.50)

print(" comeu " + str(valor) + " pesando " + str(novo) + " com gramas " + str(grama))