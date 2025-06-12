idade=str(input(" Vc tem mais do que 25 anos? " ))
idade2=int(input("Quanto exatamente? "))
ingles=str(input(" Vc fala ingles ? "))
if(idade2 <= 25 and ingles == "sim"):
    print("verdadeiro")
if(idade2 > 25 and ingles == "sim"):
    print("verdadeiro")
if(idade2 > 25 and ingles == "não"):
    print("falso")