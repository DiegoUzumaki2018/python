time=["atletico","cruzeiro"]
for k in time:
    time.append(str(input("digite o novo time")))
    if(len(time)==4):
        break
print(time)