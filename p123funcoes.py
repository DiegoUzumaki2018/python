def forma(valor,pagamento):
            vista=int(0)
            prazo=int(0)
            credito=int(0)
            if(pagamento=="vista"):
                    vista=valor*0.9
                    print(vista)
            if(pagamento=="prazo"):
                    prazo=valor*1.1
                    print(prazo)
            if(pagamento=="cartão de credito"):
                    parcelas=int(input("Quantas parcelas?"))
                    credito=valor*1.20/parcelas
                    print(credito)