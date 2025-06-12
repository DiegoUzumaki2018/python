p1=str(input("Ele voa?"))
p2=str(input("ele é rico na terra?"))
p3=str(input("ele é um deus?"))
p4=str(input("ele usa escudo?"))
p5=str(input("ele e genio?"))
t=int(0)
c=int(0)
h=int(0)
if(p1=="sim"):
   h=h+1
   t=t+1
   c=c+0
if(p2=="sim"):
   h=h+1
   t=t+0
   c=c+0
   if(p3=="sim"):
      t=t+1
      h=h+0
      c=c+0
      if(p4=="sim"):
         c=c+1
         t=t+0
         h=h+1
         if(p5=="sim"):
            h=h+1
            t=t+0
            c=c+0
 
if (p1=="não"):
   h=h+0
   t=t+0
   c=c+1

if (p2=="não"):
     h=h+0
     t=t+0
     c=c+1

if (p3=="não"):
      t=t+0
      h=h+1
      c=c+1
if(p4=="não"):
         c=c+0
         t=t+1
         h=h+0
if(p5=="não"):
      h=h+0
      t=t+1
      c=c+1

print("homem de ferro" + str(h) + "capitão america" + str(c) + "thor" + str(t))