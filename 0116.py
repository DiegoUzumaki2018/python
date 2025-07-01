import p0116funcoes as fn
divida=str(input("ta em divida?"))
if(divida=="sim"):
    t=fn.lascado(divida)
    print(f"ta devendo {t}")
if(divida=="não"):
    print("ok")
     