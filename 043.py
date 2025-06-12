pessoa1=int(input("Qual é a sua idade?"))
pessoa2=int(input("Qual é a sua idade?"))
if(pessoa1==9):
    print("mirim")
if(pessoa1>10 and pessoa1<14):
    print("infantil")
if(pessoa1>=15 and pessoa1<=18):
    print("jovem")
if(pessoa1>=19 and pessoa1<=24):
    print("adulto")
if(pessoa2==9):
    print("mirim")
if(pessoa2>=10 and pessoa2<=14):
    print("infantil")
if(pessoa2>=15 and pessoa2<=18):
    print("jovem")
if(pessoa2>=19 and pessoa2<=24):
    print("adulto")

if(pessoa1==pessoa2):
   print ("qual horario da luta")
if(pessoa1 != pessoa2):
    print("luta cancelada")

print("idade1" + str(pessoa1) + "idade2" + str(pessoa2))