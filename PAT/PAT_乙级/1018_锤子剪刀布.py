"""石头剪刀布
石头
剪刀
布
"""
from collections import Counter
num = input("请输入交手次数:")
jia_winner = 0
yi_winner = 0
jy_ping = 0
jia_win_figure = []
yi_win_figure = []
for x in range(0,int(num)):
    message = input("出手信息(甲/乙):")
    list_msg = message.split(" ")
    if list_msg[0] == 'c':
        if list_msg[1] == 'j':
            jia_winner = jia_winner+1
            jia_win_figure.append(list_msg[0])
        elif list_msg[1] == 'c':
            jy_ping = jy_ping+1
        else:
            yi_winner = yi_winner+1
            yi_win_figure.append(list_msg[1])
    elif list_msg[0] == 'j':
        if list_msg[1] == 'j':
            jy_ping = jy_ping+1
        elif list_msg[1] == 'c':
            yi_winner = yi_winner+1
            yi_win_figure.append(list_msg[1])
        else:
            jia_winner = jia_winner+1
            jia_win_figure.append(list_msg[0])
    else:
        if list_msg[1] == 'j':
            yi_winner = yi_winner+1
            yi_win_figure.append(list_msg[1])
        elif list_msg[1] == 'c':
            jia_winner = jia_winner+1
            jia_win_figure.append(list_msg[0])
        else:
            jy_ping = jy_ping+1
print(jia_winner," ",yi_winner," ",jy_ping)

def quan(l):
    counter = Counter(l)
    value = list(counter.values())
    max_value = max(value)
    for k,v in counter.items():
        if v==max_value:
            print(k)
    #for k,v in counter
quan(jia_win_figure)
quan(yi_win_figure)
