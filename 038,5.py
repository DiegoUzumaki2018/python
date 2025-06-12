salario=int(input("Qual é o salario?"))
if(salario<1518):
    salario=salario*103*0.00075
if(salario>1518 and salario<2793):
    salario=salario*103*0.00009
if(salario>2793 and salario<4190):
    salario=salario*103*0.12
if(salario>4190 and salario<9157):
    salario=salario*103*0.14
    
print("o salario é " + str(salario))