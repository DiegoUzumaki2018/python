contador=int(0)
soma=int(0)
tentativas=int(0)
while (contador!=99999):
        contador=contador+1
        digite=int(input("digite o numero"))
        if(digite==999):
            break
        soma+=digite
        tentativas=contador
print(str(soma) + str(tentativas))      