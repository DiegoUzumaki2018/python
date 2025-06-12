idade1=int(input("qual é sua idade"))
idade2=int(input("qual é sua idade"))
idade3=int(input("qual é sua idade"))
idade4=int(input("qual é sua idade"))
maior=int(0)
menor=int(99999)
if(idade1>maior):
    maior=idade1
if(idade2>maior):
    maior=idade2
if(idade3>maior):
    maior=idade3
if(idade4>maior):
    maior=idade4
if(idade1<menor):
    menor=idade1
if(idade2<menor):
    menor=idade2
if(idade3<menor):
    menor=idade3
if(idade4<menor):
    menor=idade4

print(" mais jovem" + str(menor)+ " mais velho" + str(maior))
    
