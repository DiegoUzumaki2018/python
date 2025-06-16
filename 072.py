import random
cont=int(0)
soma=int(0)
while(cont!=9999):
        cont=cont+1
        number=random.randint(1,9)
        num=int(input("digite um numero"))
        soma=num+number
        if(soma%2==0 and num%2==0):
            print("ganhou")
            print(f"suas derrotas foram {cont}")
            break
        if(soma%2==1 and num%2==1):
            print("ganhou")
            print(f"suas derrotas foram {cont}")
            break
        else:
             print("perdeu")

        
        
