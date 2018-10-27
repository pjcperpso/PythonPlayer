"""将依据英语倒序输出"""
s = "please input this word"
list_s = s.split(" ")
s = ""
for x in range(0,len(list_s))[::-1]:
    s = s+list_s[x]+" "
print(s)
