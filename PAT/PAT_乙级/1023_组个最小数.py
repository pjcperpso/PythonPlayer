"""给定个数小于10的几个数
要求组成最小数   0不能做首位
如：00121123-------10011223
思路利用排序算法将数字从小到大排列
取出第一个为不为0的数和第一个互换
在调用list转换成str的方法
首位不能为0
"""
list = [0,1,2,3,5,6,1,1,1]
for x in range(0,len(list)):
    temp = 0
    for y in range(0,len(list)-x-1):
        if list[y]>list[y+1]:
            temp = list[y]
            list[y] = list[y+1]
            list[y+1] = temp
num = 0
for x in list:
    if x!=0:
        print(x,num)
        break;
    num = num+1
temp1 = 0
temp1 = list[num]
list[num] = list[0]
list[0] = temp1

new_list = [str(x) for x in list]
print("".join(new_list))
