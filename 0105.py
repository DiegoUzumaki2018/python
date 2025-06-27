import random

c=int(input("Quanto de dinheiro você tem?"))
b=int(input("Qual é o valor a ser apostado?"))
d=random.randint(2,10)
print("[1] quer multiplicar por 1.1?")
print("[2] quer multiplicar por 1.3?")
print("[3] quer multiplicar por 1.6?")
print("[4] quer multiplicar por 2?")
print("[5] quer multiplicar por 2.5?")
a=float(input("Qual é a vc escolhe?"))

match a:
    case 1:
        b=b*d
    case 2:
        b=b*d
    case 3:
        b=b*d
    case 4:
        b=b*d
    case 5:
        b=b*d
print(b)