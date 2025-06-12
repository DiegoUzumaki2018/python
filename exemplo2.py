a=int(input("maior"))
if(a>10):
   print("deu certo")
else:
   print("não deu certo")
if(a>10 and a<20):
   print("deu certo")
elif(a> 20 or a <30): #elif equivale a senão se
    print("deu certo 2")
else:
    print("deu errado")

import random

a=int(random.randint(10,20))
print(a)