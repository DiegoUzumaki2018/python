contador=int(0)
grupo=int(0)
grupo2=int(0)
grupo3=int(0)
grupo4=int(0)
while (contador !=999999):
        contador=contador+1
        numeros=int(input("escreva o numeros"))
        if(numeros>0 and numeros<25):
                grupo=grupo+1
                print("os numeros estao entre [0-25]")
                parar=str(input("deseja continuar?"))
                if(parar=="não"):
                    break
        if(numeros>26 and numeros<50):
                grupo2=grupo2+1
                print("os numeros estao entre [26-50]")
                parar=str(input("deseja continuar?"))
                if(parar=="não"):
                    break
        if(numeros>51 and numeros<75):
                grupo3=grupo3+1
                print("os numeros estao entre [51-75]")
                parar=str(input("deseja continuar?"))
                if(parar=="não"):
                    break
        if(numeros>76 and numeros<100):
                grupo4=grupo4+1
                print("os numeros estao entre [76-100]")
                parar=str(input("deseja continuar?"))
                if(parar=="não"):
                    break              
print(f"tem tantos no {grupo} tem tantos {grupo2} tem tantos {grupo3} tem tantos {grupo4}")