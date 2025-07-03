def escolha(a):
    match a:
        case 1:
            cidade=str(input("Qual cidade?"))
            idade=int(input("Sua idade?"))
            print(f"você tem {idade} anos e mora na cidade {cidade}")
        case 2:
            peso=int(input("Qual é seu peso?"))
            altura=int(input("Qual é a sua altura?"))
            print(f"sua altura é {altura} e seu peso é {peso}")
        case 3:
            cor=str(input("Qual é a cor do seu cabelo?"))
            pé=int(input("Qual é o tamanho do seu pé"))
            print(f"a cor do seu cabelo é {cor} e sua altura é {pé}")