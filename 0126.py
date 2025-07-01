import p0126funcoes as fn
n1=int(input("Digite um numero"))
n2=int(input("Digite um numero"))
t=fn.maior(n1,n2)
r=fn.menor(n1,n2)
media=int(0)
media=t/r
print("o maior é " + str(t))
print("o menor é " + str(r))
print("a media é " + str(media))


