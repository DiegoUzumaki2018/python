contador=int(0)
maior=int(0)
menor=int(0)
nome2=str("")
nome3=str("")
while (contador !=5):
        contador=contador+1
        sexo=str(input("Qual é seu sexo?"))
        idade=int(input("Qual é a sua idade?"))
        nome=str(input("Qual é seu nome"))
        if(idade>maior):
                maior=maior+idade
                nome2=nome
        if(idade<menor):
                menor=menor+idade
                nome3=nome3+nome
print(f"o mais velho é {nome2}{maior} e o mais nova é {nome3}{menor}")