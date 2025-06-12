numero1=int(input("digite o numero"))
numero2=int(input("digite o numero"))
maior=int(0)
menor=int(9999)
igual=int(0)
if(numero1 == numero2 ):
    igual=igual
    print("Os numeros são iguais por isso não existe maior ou menor")

if(numero1 != numero2): 
    if(numero1>maior):
        maior=numero1
    if(numero2>maior):
        maior=numero2
    if(numero1<menor):
        menor=numero1
    if(numero2<menor):
        menor=numero2
        
print(str(maior)+str(menor))