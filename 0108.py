import random 
a=random.randint(1,3)
for cont in range(1,5,1):
 b=int(input("Escolha:[1]Pedra,[2]Papel,[3]Tesoura"))
 if(b==1 and a==1):
    print("empate")
 if(b==2 and a==2):
    print("empate")
 if(b==3 and a==3 ):
    print("empate")
 if(b==1 and a==2):
    print("ganhou")
 if(b==2 and a==3):
    print("ganhou")
 if(b==3 and a==1):
        print("ganhou")
 if(a==1 and b==2):
     print("perdeu")
 if(a==2 and b==3):
     print("perdeu")
 if(a==3 and b==1):
    print("perdeu")


