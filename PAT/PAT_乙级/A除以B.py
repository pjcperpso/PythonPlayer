"""
给一个超大数 求商和余数
思路：俩俩组成十位数 相除
"""
s = input("请输入数字:")
chushu = int(input("请输入除数:"))
temp_y = 0
temp = 0
num = 0
L_s = []
for x in s:
    num = num+1
    if num==2:
        temp_y = int(s[0:2])%chushu
        L_s.append(str(int(s[0:2])//chushu))
    if num>2:
        temp = (int(x)+temp_y*10)
        L_s.append(str(temp//chushu))
        temp_y = temp%chushu

final_s = "".join(L_s)
print(final_s,temp_y)
