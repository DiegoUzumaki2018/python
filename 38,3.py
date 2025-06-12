valor=int(input("Qual é o valor da compra?"))
forma=str(input("Qual forma de pagamento?"))

if(valor=="pix" or "dinheiro"):
    forma=valor*0.15
    print(forma)
if(valor=="debito"):
    forma=valor*0.10
    print(forma)
if(valor=="cartão de credito"):
    parcelas=str(input("Quantas parcelas?"))
if(parcelas=="duas vezes"):
    parcelas=valor*valor
if(parcelas=="três vezes"):
    parcelas=valor+0.10
    