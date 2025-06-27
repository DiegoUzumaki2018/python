valor=[0,0,0,0]
vista=int(0)
boleto=int(0)
debito=int(0)
cont=int(0)
soma=int(0)
for k in valor:
        valor[cont]=int(input("Qual é o valor do produto?"))
        quer=str(input("Quer parar?"))
        if(quer=="s"):
                qual=str(input("Qual é a forma de pagamento?"))
                if(qual=="vista"):
                        soma=soma+valor[cont]
                        vista=soma*0.90
                        print(vista)
                        break
                if(qual=="boleto"):
                        soma=soma+valor[cont]
                        boleto=soma*1.10
                        print(boleto)
                        break
                if(qual=="debito"):
                        soma=soma+valor[cont]
                        debito=soma*0.95
                        print(debito)
                        break
    