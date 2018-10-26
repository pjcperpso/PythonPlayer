def Continue():
    L = [3,5,7,6,8,11]
    L1 = []
    num = []
    for n in L:
        if n in L1:
            continue
        num.append(n)
        while True:
            if n==1:
                break
            else:
                if n%2==0:
                    n = n/2
                    L1.append(n)
                else:
                    n=(3*n+1)/2
                    L1.append(n)
    num.sort(reverse=True)
    return num
print(Continue())
