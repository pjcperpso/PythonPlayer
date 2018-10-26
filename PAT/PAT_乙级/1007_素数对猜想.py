"""思路：
先求出指定范围内的所有素数
将素数添加至列表
最后遍历列表依次相减取差为2的个数
"""
def Sushu():
    """指定范围求素数"""
    factor = input("please input factor:")
    L = []
    for x in range(2,int(factor)+1):
        num = 0
        for y in range(2,x+1):
            if x%y==0:
                num = num+1
        #print(num)
        if num==1:
            """添加至列表"""
            L.append(x)
    print(L)
    """遍历列表求差为二的素数个数"""
    sum = 0
    for x in range(0,len(L)-1):
        if L[x+1]-L[x]==2:
            sum = sum+1
    print(sum)
Sushu()
