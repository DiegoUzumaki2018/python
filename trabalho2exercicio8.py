valor=float(input("Qual é o valor do produto?"))
print("[1] pix ou a vista")
print("[2] cartão de debito")
print("[3] cartão de credito")
pagamento=int(input("Qual é a forma de pagamento"))
match pagamento:
        case 1:
            valor=valor*0.10
            print(f"desconto {valor}")
        case 2:
            valor=valor*0.5
            print(f"desconto{valor}")
        case 3:
            parcelas=int(input("Quantas parcelas?"))
            valor2=int(0)
            total=int(0)
            if(parcelas<=3):
                    valor2=valor*0.5
                    total=valor2+valor
                    print(f"sua compra de {valor} parcelada em {parcelas} de {valor2} sendo um total de {total}")
            if(parcelas>3):
                    valor2=valor*0.10
                    total=valor2+valor
                    print(f"sua compra de {valor} parcelada em {parcelas} de {valor2} sendo um total de {total}")