cont=int(0)
multa=int(2)
while (cont !=200):
        usuario=str(input("Qual usuario?"))
        senha=str(input("Qual é a senha?"))
        if(usuario=="aa" and senha=="bb"):
                    print("correto")
                    break
        else:
                multa=multa*2
                print(f"vc sera multa novamente {multa}")