def lascado(divida):
        pessoa=int(input("Quanto é a divida?"))
        tempo=int(input("Quanto tempo?"))
        taxa=int(input("Qual é a taxa?"))
        total=int(0)
        juros=int(0)
        juros=pessoa*tempo*taxa
        total=pessoa+juros
        return total