import p0127funcoes as fn
cargo=str(input("Qual é seu cargo?"))
mult=int(0)
t=fn.analisar(cargo)
mult=t*12
print("o valor da renda anual é " + str(mult))
