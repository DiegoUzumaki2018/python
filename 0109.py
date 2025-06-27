import random 
a=random.randint(0,4)
cont2=int(0)
for cont in range (1,6,1):
         b=int(input("Qual:[0] Pedra [1] Papel [2] Tesoura [3] Largato [4] Spock"))
         if(a==0 and b==2):
           print("perdeu")
         if(a==2 and b==1):
           print("perdeu")
         if(a==1 and b==0):
           print("perdeu")
         if(a==3 and b==1):
           print("perdeu")
         if(a==4 and b==0):
           print("perdeu")
         if(a==0 and b==3):
           print("perdeu")
         if(a==2 and b==4):
           print("perdeu")
         if(a==1 and b==4):
           print("perdeu")
         if(a==3 and b==4):
           print("perdeu")
         if(b==0 and a==2):
           print("ganhou")
         if(b==2 and a==1):
           print("ganhou")
         if(b==1 and a==0):
           print("ganhou")
         if(b==3 and a==1):
           print("ganhou")
         if(b==4 and a==0):
           print("ganhou")
         if(b==0 and a==3):
           print("ganhou")
         if(b==2 and a==4):
           print("ganhou")
         if(b==1 and a==4):
           print("ganhou")
         if(b==3 and a==4):
           print("ganhou")
         if(b==0 and a==0):
           print("empate")
         if(b==1 and a==1):
           print("empate")
         if(b==2 and a==2):
           print("empate")
         if(b==3 and a==3):
           print("empate")
         if(b==4 and a==4):
           print("empate")

