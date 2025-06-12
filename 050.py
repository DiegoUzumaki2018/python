print("soma")
print("subtração")
print("multiplicação")
print("divisão")
a=str(input(""))
b=int(input("digite um numero"))
c=int(input("digite um numero"))
soma=int(0)
subtrasao=int(0)
multiplicasao=int(0)
divisao=int(0)
match a:
    case "soma":
        soma=b+c
        print(soma)
    case "subtração":
        subtrasao=b-c
        print(subtrasao)
    case "mulplicação":
        multiplicasao=b*c
        print(multiplicasao)
    case "divisão":
        divisao=b/c
        print(divisao)