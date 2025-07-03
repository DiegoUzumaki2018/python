sindicato=int(0)
inss=int(0)
liquido=int(0)
desconto=int(0)
quanto=int(input("Quanto vc recebe?"))
sindicato=quanto*0.8
inss=quanto*0.05
liquido=quanto*0.11
desconto=quanto+liquido+inss+liquido
print(f"é os descontos {desconto}")