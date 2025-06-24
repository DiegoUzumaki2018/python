francisco=float(1.50)
sara=float(1.10)
cont=int(0)
while(cont !=999):
            cont=cont+1
            sara=sara*0.03
            francisco=francisco*0.02
            if(sara>francisco):
                    break
print(f"a sara e maior com {sara} e o francisco {francisco}")
