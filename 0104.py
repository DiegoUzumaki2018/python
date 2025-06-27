import random

mult=int(4)
mult2=int(8)
dinh=int(input("Quanto vc tem de dinheiro?"))
soma=int(0)
perdeu=int(0)
for cont in range(999):
        v=random .randint(1,3)
        print(v)
        aposta=int(input("Quanto voce quer apostar?"))
        if(aposta>dinh):
                break
        a=int(input("Qual:[1] Vermelho [2] Petro [3] Branco"))
        
        if(a==1 and  v==1):
                mult=mult*2
                dinh=dinh+mult
                print(f"vc ganhou {dinh}")
        if(a==2 and v==2):
                mult=mult*2
                dinh=dinh+mult
                print(f"vc ganhou {dinh}")
        if(a==3 and v==3):
                mult=mult*14
                dinh=dinh+mult
                print(f"vc ganhou {dinh}")
                quer=str(input("quer continuar"))
                if(quer=="n"):
                        print(f"seu saldo ficou {dinh} \n")
                        break
                if(quer=="s"):
                        print(f"seu saldo ficou {dinh} \n")
              
        

