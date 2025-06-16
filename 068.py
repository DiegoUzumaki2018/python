contador=int(0)
multa=int(1)
while (contador !=200):
        usuario=str(input("Digite o usuario"))
        senha=str(input("digite a senha"))
        if(usuario=="facil" and senha=="ff"):
                    print("acesso correto")
                    break
        else:
                multa=multa*2
                print(f"vc sera multado {multa} tente novamente")
