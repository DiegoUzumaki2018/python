valor=int(input("Qual é o valor da compra"))
if(valor>500):
    valor=valor*0.5
else:
    valor=valor

print("O valor final da sua compra é" + str(valor))