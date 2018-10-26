def print_this(n):
    B_wei = int(n/100)
    S_wei = int(n/10%10)
    G_wei = int(n%10)
    L = []
    for x in range(0,B_wei):
        L.append('百')
    for x in range(0,S_wei):
        L.append('十')
    L.append(str(G_wei))
    result = "".join(L)
    print(result)
print_this(569)
