print("básico")
print("intermediario")
print("avançado")
excel=str(input("Qual é seu nivel de excel?"))



match excel:
    case "básico":
        basico=str(input("qual?"))
        if(basico=="soma"):
            print("vc vai somar")
        if(basico=="média"):
            print("vc vai fazer a média")
        if(basico=="maximo"):
            print("vc vai fazer o maximo")
    case "intermediario":
        intermediario=str(input("qual?"))
        if(intermediario=="se"):
            print("vc vai fazer o se")
        if(intermediario=="somase"):
            print("vc vai fazer a somase")
        if(intermediario=="cont.se"):
            print("vc vai vai cont.se")
    case "avançado":
        avansado=str(input("qual?"))
        if(avansado=="ordem"):
            print("vc vai ordenar")
        if(avansado=="procv"):
            print("vc vai fazer procv")
        if(avansado=="proch"):
            print("vc vai fazer pohach")