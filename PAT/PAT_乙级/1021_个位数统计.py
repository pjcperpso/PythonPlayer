"""
利用双重循环取值
再用map的特点  去重复   来存键值对
"""
s = "100311"
jian = {}
for x in range(0,len(s)):
    num = 0
    for y in range(0,len(s)):
        if s[y] == s[x]:
            num = num+1
    jian[s[x]]=num

for k,v in jian.items():
    print(k,":",v)
print(jian)
