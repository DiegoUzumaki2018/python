def cobrar(km):
        total=int(0)
        dias=int(input("quantos dias percorrido?"))
        dias=dias*60
        km=km*0.15
        total=dias+km
        return total