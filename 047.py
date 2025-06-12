distancia=int(input("Qual é a distancia percorrida?"))
if(distancia<=200):
    distancia=distancia*0.35
if(distancia>=200):
    distancia=distancia*0.20
    bairro=str(input("O bairro é perigoso?"))
    if(bairro=="perigoso" and distancia>200):
        distancia=distancia*1.8
    print("o valor final é" + str(distancia))