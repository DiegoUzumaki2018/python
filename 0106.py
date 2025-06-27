import random
b=random.randint(1,999)
cont=int(0)
while(cont!=999):
        cont=cont+1
        
        a=str(input("E a sua primeira vez?"))
        c=int(input("Quanto tu tem?"))
        if(a=="sim" and cont==1):
                a=a=b
                print(a)
        if(a=="não"):
                a=a=b
                print(a)
        c=str(input("Quer ir de novo?"))
        if(c=="sim"):
            if(a==b):
                b=b