numero1=int(input("Qual é o valor?"))
numero2=int(input("Qual é  outro valor"))
operação=str(input("Qual operação vc quer?"))
if(operação=="soma"):
    soma=int(numero1+numero2)
    print(soma)
if(operação=="subtração"):
    subtração=int(numero1-numero2)
    print(subtração)
if(operação=="multiplicação"):
    multiplicação=int(numero1*numero2)
    print(multiplicação)
if(operação=="divisão"):
    divisão=int(numero1/numero2)
    print(divisão)