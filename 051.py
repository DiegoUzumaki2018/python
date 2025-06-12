peso=int(input("Qual é o peso da terra?"))
print("Mercurio")
print("venus")
print("marte")
print("jupiter")
print("saturno")
print("urano")
t=str(input("Escolha um planeta"))
match t:
    case "Mercurio":
        peso=peso*0.37
    case "venus":
        peso=peso*0.88
    case "marte":
        peso=peso*0.38
    case "jupiter":
        peso=peso*2.64
    case "saturno":
        peso=peso*1.15
    case "urano":
        peso=peso*1.17

print("se vc estivesse no planeta " + t +"vc pensaria " + str(peso))