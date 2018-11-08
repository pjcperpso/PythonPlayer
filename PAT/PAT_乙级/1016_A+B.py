"""给出正整数
A=3023223
DA=2       求出DA在A中的个数    组成新的整数
PA=222
"""
message = input("请输入数据:")
one = message.split(" ")
#D_A = 2
#A = "302206202"

def new_date(D_A,A):
    L = []
    for x in A:
        if x==D_A:
            L.append(x)
    final = "".join(L)
    return int(final)
last_date = new_date(one[1],one[0])+new_date(one[3],one[2])
print(last_date)
