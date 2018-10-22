"""
偶数:/2.......
奇数：(3n+1)/2.......
某一步:n=1
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
    print(sum)
    
Callatz(3)
