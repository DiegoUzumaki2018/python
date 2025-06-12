casa=int(input("Qual valor da casa?"))
salario=int(input("Qual seu salario?"))
meses=int(input("Quantos meses vai pagar?"))
exceder=float(casa*0.30)
if(exceder>salario):
    print("empréstimo será negado")
else:
    print("juros financiado")