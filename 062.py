pesomedio=int(70)
contador=int(0)
contador2=int(0)
contador3=int(0)
while(contador !=4):
        contador=contador+1
        pessoas=int(input("seu peso"))
        if(pessoas<pesomedio):
            contador2=contador2+1
        else:
            contador3=contador3+1
print(f" existe {contador2} que estão acima do peso médio e existe {contador3} com peso igual ou abaixo a media")    
