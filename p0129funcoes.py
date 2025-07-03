def converter(a,b):
    dolar=int(0)
    euros=int(0)
    iene=int(0)
    if(b=="dólares"):
        dolar=a*5.46
        print("voce tem equivalente a "  + str(dolar) + "dólares")
    
    if(b=="euros"):
        euros=a*6.44
        print("voce tem equivalente a "  + str(euros)  + "euros")
      
    if(b=="iene"):
        iene=a*0.038
        print("voce tem equivalente a "  +  str(iene) +"iene")
        