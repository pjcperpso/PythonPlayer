"""
十进制转八进制
除8取余法
120：120/8=15.....0
15/8=1.....7
1/8=0......1
"""
list = []
num = 123+456
while True:
    if num==0:
        break
    else:
        x = num%8
        num = int(num/8)
        print(x,num)
        list.append(x)
sum = 0
for x in range(0,len(list)):
    cheng = 1
    for y in range(0,x):
        cheng = cheng * 10
    sum = sum+list[x]*cheng
    print(sum)
