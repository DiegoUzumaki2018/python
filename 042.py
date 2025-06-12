nota1=int(input("Qual é a nota do primeiro aluno"))
nota2=int(input("Qual é a nota do segundo aluno"))
media=int(nota1+nota2/2)
fre=int(input("Qual frequencia?"))

if(media>=60 and fre>=75):
    print("aprovado")
if(media>40 and media<60):
    print("esta de recuperação")
    nr=float(input("Qual é a nota de recuperação? "))
    if(media<40):
        print("reprovado sem direito a recuperação")

    elif(nr<=69.99):
        print("reprovado")
    else:
        print("aprovado")
    