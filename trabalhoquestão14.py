humorista=str(input("Qual humorista?"))
cidade=str(input("Qual é a sua cidade?"))
if(cidade=="São Paulo" and humorista=="Danilo"):
        print("tem show do Danilo Gentili")
elif(cidade=="Araxa" and humorista=="Fabio Porchat"):
        idade=int(input("qual é a sua idade?"))
        if(idade==18):
            print("tem show")


elif(cidade=="Rio Grande do Sul" and humorista=="Rafinha Bastos"):
        print("tem show")
else:
         print("não tem show")