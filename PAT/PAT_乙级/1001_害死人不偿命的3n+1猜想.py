"""
偶数:/2.......
奇数：(3n+1)/2.......
第n步:n=1
求n=？
"""

def Callatz(n):
    sum = 0
    while True:
        if n==1:
            break
        if n%2==0:
            n/=2
            sum+=1
        else:
            n=(3*n+1)/2
            sum+=1
    return sum

print(Callatz(3),'次')
