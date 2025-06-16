cont=int(0)
contpares=int(0)
contimpares=int(0)
somapar=int(0)
somaimpar=int(0)
somageral=int(0)
for cont in range(0,4,1):
            numero=int(input("digite um numero"))
            if(numero%2==0):
                    contpares=contpares+1
                    somapar=somapar+numero
            if(numero%2==1):
                    contimpares=contimpares+1
                    somaimpar=somaimpar+numero


                    somageral=somaimpar+somapar
print(f"foram cadastrado {contpares} números pares, foram cadastrados {contimpares} numeros impares, a soma dos pares é {somapar} a soma dos impares é {somaimpar}, a soma geral é {somageral} ")