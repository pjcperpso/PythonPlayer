def write(i):
    L = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
    chinese = str(i)
    for x in range(0,len(chinese)-1):
        sum = int(chinese[x])+int(chinese[x+1])
        if sum>=1 and sum<=9:
            print(L[sum])
        else:
            print('yi',L[sum%10])

write(152456156565456468654)
