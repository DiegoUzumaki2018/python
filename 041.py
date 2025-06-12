quanto=int(input("Quando vendeu esse mês"))
if(quanto>=22.000):
    tempo=int(input("Quanto tempo vc ta empresa?"))
if(tempo==2):
    quanto=quanto*0.3
if(tempo>=3):
    quanto=quanto*0.4
if(tempo<2):
    quanto=quanto*0.2

print("A comissao é " + str(quanto))