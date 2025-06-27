a=int(input("Qual é o valor?"))
print("[1] vista ou pix?")
print("[2] cartão de debito")
print("[3] cartão de credito?")
b=int(input("Qual dessas formas de pagamento?"))
a2=int(0)
match b:
    case 1:
        a=a*0.10
        print(f"o desconto é {a}")
    case 2:
        a=a*0.05
        print(f"o desconto é {a}")
    case 3:
        c=int(input("Quantas parcelas?"))
        if(c<=3):
            a2=a2*0.05
            print(f"sua compra de {a} parcelada em {c} de {c} sendo o total de {a2}")
        if(c>=10):
            a2=a2*0.10
            print(f"sua compra de {a} parcelada em {c} de {c} sendo o total de {a2}")