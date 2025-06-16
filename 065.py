contandor=int(0)
soma=int(0)
positivo=int(0)
negativo=int(0)
while (contandor !=9999):
            contandor=contandor+1
            digite=int(input("Digte um numero"))

            if (digite >0):
                    positivo=contandor
            if(digite<0):
                negativo=contandor
            parar=str(input("Quer parar?"))
            if(parar =="sim"):
                    soma=soma+digite
                    break
print(f"a media dos valores é {soma} e a quantidades de positivos é {positivo} e a quantidade de negativos {negativo}")
                    