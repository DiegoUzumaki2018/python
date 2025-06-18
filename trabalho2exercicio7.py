print("[1] dengue")
print("[2] gripe")
print("[3] covid 19")
print("[4] asma")
doensa=int(input("Qual dessas doenças?"))
match doensa:
        case 1:
            print("Febre alta, entre 39 e 40ºC;Náuseas e vômitos;Dor de cabeça")
        case 2:
            print("Espirros e nariz escorrendo ou entupido;Calafrios;Dor de garganta;Perda de apetite")
        case 3:
          print("Garganta inflamada;Febre acima de 38º C;Coriza ou nariz entupido")
        case 4:
          print("Falta de ar;Chiado no peito;Tosse seca")
          