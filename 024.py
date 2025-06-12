numero1=int(input(" digite um numero "))
numero2=int(input(" digite outro numero "))
pergunta=str(input(" soma ou media? "))
if(pergunta == "soma"):
    soma=int( numero1+numero2)
    print(" soma de " + str (numero1) + str (numero2)  + " é igual a " +  str (soma))
if(pergunta == "media"):
    media=int(numero1+numero2/3)
    print(" media de " +  str( numero1 )  +  str( numero2 )  + " é igual a " + str (media))