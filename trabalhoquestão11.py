planeta=str(input("Qual planeta"))
peso=float(input("QUal é o peso?"))
if(planeta == "Mercurio"):
    peso=peso*0.37
if(planeta=="venus"):
    peso=peso*0.88
if(planeta=="marte"):
    peso=peso*0.38
if(planeta=="jupiter"):
    peso=peso*2.64
if(planeta=="saturno"):
    peso=peso*1.15
if(planeta=="urano"):
    peso=peso*1.17


print("Se vc estivesse no planeta" + planeta +" vc pesaria " + str(peso))