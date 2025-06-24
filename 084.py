cont=int(0)
quant=int(0)
quant2=int(0)
quant3=int(0)
for cont in range(0,4,1):
            nome=str(input("Qual seu tipo de padrão?"))
            valor=int(input("Qual é o valor?"))
            quer=str(input("Quer fechar?"))
            if(quer=="sim"):
                    break
            
            if(nome=="a" and valor>1000):
                    quant=quant+1
            if(nome=="b" and valor>500 and valor<999):
                    quant2=quant2+1
            if(nome=="c" and valor<499):
                    quant3=quant3+1

print(str(quant) + str(quant2) + str(quant3))