"""数素数
给定一个范围  从中找取所有素数
每十个占一行  行尾不允许有空格
用字符串拼接  十个一循环
"""
sushu = []
"""求出指定范围内素数"""
def Ss():
    for x in range(20,150):
        s = 0
        for y in range(1,x):
            if x%y==0:
                s+=1
        if s==1:
            sushu.append(str(x))
    return sushu
m = 0
for x in range(0,len(Ss())):
    if (x+1)%10==0:
        print(' '.join(Ss()[m*10:m*10+10]))
        m+=1
