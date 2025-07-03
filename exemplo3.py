print("O que você prefere")
print("[1] pastel de carne")
print("[2] pastel de queijo")
print("[3] pastel de frango")
r=int(input(""))




match r:
    case 1:
        print("gsota de carne")
    case 2:
        print("gosta de queijo")
    case 3:
        print("gosta de frango")
    case _:
        print("opção invalida")

match r:
    case "carne":
        print("gosta de carne")
    case "queijo":
        print("gosta de queijo")

    case "frango":
        print("gosta de frango")





