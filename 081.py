cont=int(0)
soma=int(0)
cont2=int(0)
while(cont !=9):
        cont=cont+1
        digite=int(input("Digite um numero"))
        if(digite==999):
                break
        
        soma=soma+digite
        cont2=cont

print(f"a soma desses valores é {soma} e a quantidades de tentativas é {cont2}")