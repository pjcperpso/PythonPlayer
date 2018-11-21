"""
思路:
分两种情况:
        若结果为6541
            break
        否则
            最大值-最小值
求一个数组成数字可组成的最大数值和最小数值
最大数值-最小数值
"""


cishu = 0
num = "6767"
while True:
    if num == "6174" or num =="0":
        break
    else:
        max = "".join(sorted(num,reverse=True))
        min = "".join(sorted(num))
        num = str(int(max)-int(min))
        cishu = cishu+1
        print(max+"-"+min+"="+str(num))
