preso=int(input("Qual é o preço do produto? "))
print("carnaval")
print("ferias escolares")
print("dia das crianças")
print("black friday")
print("natal")
epoca=str(input("Qual é a epoca do ano?"))
match epoca:
        case "carnaval":
                preso=preso*1.10
        case "ferias escolares":
                preso=preso*1.20
        case "dia das crianças":
                preso=preso*1.05
        case "black friday":
                preso=preso*0.70
        case "natal":
                preso=preso*0.95

print("o preço final nessa data é " + str(preso))