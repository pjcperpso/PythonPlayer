"""
给出月饼种类数
"""
s = '18 15 10'
price = '75 72 45'
print(len(s))
map_Dan = {}
price_list = price.split(" ")
s_list = s.split(" ")
for num in range(0,len(price_list)):
    danjia = int(price_list[num])/int(s_list[num])
    map_Dan[danjia] = s_list[num]
print(map_Dan)

max_price = []
for key in map_Dan:
    max_price.append(key)
max_price = sorted(max_price,reverse=True)
zongshu = 0
jiedian = 0
for x in range(0,len(max_price)):
    if zongshu>=20:
        break
    zongshu=zongshu+int(map_Dan[max_price[x]])
    jiedian = jiedian+1
sum_price = 0
print(max_price)
for x in range(0,jiedian-1):
    sum_price = sum_price+int(map_Dan[max_price[x]])*round(max_price[x],2)
    print(sum_price)
sum_price = sum_price+int(map_Dan[max_price[jiedian]])*round((max_price[jiedian]),2)
print(zongshu,jiedian)
print(sum_price)
