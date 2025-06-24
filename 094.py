cont=int(0)
cont2=int(0)
while(cont!=3):
        cont=cont+1
        nome=str(input("Qual é seu nome?"))
        sexo=str(input("Qual é seu sexo?"))
        if(sexo=="h"):
                cont2=cont2+1
print(f"foram cadastrados {cont2} homens")