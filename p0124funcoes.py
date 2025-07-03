def analisar(a,b,c):
    maior=int(0)
    menor=float('inf')
    
    if(a>maior):
        maior=a
    if(b>maior):
        maior=b
    if(c>maior):
        maior=c
    if(a<menor):
        menor=a
    if(b<menor):
        menor=b
    if(c<menor):
        menor=c
    
    print(" o maior é " + str(maior))
   