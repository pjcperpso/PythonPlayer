i = 17
sum = 0
L = []
for x in range(1,19,2):
    L.append(x)
    sum = sum+x
    if(sum*2>int(i)):
        break
zifu = []
for x in L:
    zifu.append("*")
for x in range(0,len(L)):
    for y in range(0,L[x]):
        zifu[y] = "0"
    print(zifu)
