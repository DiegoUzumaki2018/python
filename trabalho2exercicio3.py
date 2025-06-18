cont=int(0)
contnum=int(0)
contnum2=int(0)
contnum3=int(0)
contnum4=int(0)
while (cont !=99999):
        cont=cont+1
        numero=int(input("Digite o numero"))
        if(numero>10 and numero<20):
                contnum=contnum+1
                yes=str(input("Quer continuar?"))
                if(yes=="não"):
                        break
        if(numero>21 and numero<30):
                contnum2=contnum2+1
                yes=str(input("Quer continuar?"))
                if(yes=="não"):
                        break
        if(numero>31 and numero<40):
                contnum3=contnum3+1
                yes=str(input("Quer continuar?"))
                if(yes=="não"):
                        break
        if(numero>76 and numero<100):
                contnum4=contnum4+1
                yes=str(input("Quer continuar?"))
                if(yes=="não"):
                        break
print(f"no total é {contnum} numeros entre 10-20; {contnum2} numeros entre 21-30;{contnum3} numeros entre 31-40;{contnum4}numeros entre 76-100")