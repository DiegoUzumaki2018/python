print("Fabio Porchat")
print("Danilo Gentil")
print("Rafinha Bastos")
humor=str(input("Qual é humorista"))
cidade=str(input("qual é a cidade?"))
match humor:
    case "Fabio Porchat":
        idade=int(input("Quantos anos vc tem?"))
        if(cidade=="Araxá" and idade>18):
               print("tem show")
        else:
             print("não tem show")
    case "Danilo Gentil":
          if(cidade=="São Paulo"):
               print("tem show")
          else:
            print("não tem show")
    case "Rafinha Bastos":
          if(cidade=="Rio Grande do sul"):
               print("tem show do Rafinha Bastos")
          else:
               print("não tem show")