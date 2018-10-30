"""
思路 四个字符串中 两两比较 第一对取出星期和小时
                         第二对取出分钟
利用字典的键值对形式存放星期和小时
"""
#map = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"k":20,"L":21,"M":22,"N":23,"O"}
S = "123456789ABCDEFGHIGKLMNO"
dict_hours = {}
dict_Xingqi = {}
"""存储星期"""
L_Xingqi = ['MON','TUE','WED','THU','FRI','SAT','SUN']
"""将星期和小时以键值对的形式存储在字典"""
for x in range(1,len(S)+1):
    if x<8:
        dict_Xingqi[S[x+8]] = L_Xingqi[x-1]
    dict_hours[S[x-1]] = x

print(dict_hours)
print(dict_Xingqi)
"""测试"""
one = '3485djDkxh4hhGE'
two = '2984akDfkkkkggEdsb'
three = 's&hgsfdk'
four = 'd&Hyscvnm'
num = 0
cihus = 0
final = []
if len(one)<len(two):
    num = len(one)
else:
    num = len(two)
for x in range(0,num):
    if one[x]==two[x]:
        final.append(one[x])

if len(three)<len(four):
    num = len(three)
else:
    num = len(four)
import re
minute = ''
right = re.compile(r'[A-Za-z]')
for x in range(0,num):
    if three[x]==four[x] and right.match(three[x]):
        if x<10:
            minute = "0"+str(x)
        else:
            minute = str(x)
first_x = 0
for x in range(0,len(final)):
    if final[x] in S[9:]:
        break
    first_x+=1
print(dict_Xingqi[final[first_x]],str(dict_hours[final[first_x+1]])+':'+minute)
