a=[3,6,12,24,48,96,192,384,768,1536]

for k in a:
        if(k==3 or k==6 or k==96):
                print(f"${k}$")
        else:
                print(k)
print("-------------")
a=[3,0,0,0,0,0,0,0,0,0,0,0]
cont=int(0)
for cont in range(10):
        a[cont+1]=a[cont]*2
        if(a[cont]==3 or a[cont]==6 or a[cont]==96):
                print(f"${a[cont]}")
        else:
                print(a[cont])