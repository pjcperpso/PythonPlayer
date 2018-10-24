"""
3
Joe Math990112 89
Mike CS991301 100
Mary EE990830 95

Mike CS991301
Joe Math990112
"""
def ChengjiSort():
    num = input("please input ceshi num:")
    dic = {}
    Chengji = []
    for x in range(0,int(num)):
        msg = input("please input msg:")
        message = msg.split(" ")
        """键值对形式存值"""
        dic[message[2]]=message[0]+" "+message[1]
        Chengji.append(int(message[2]))
    print(Chengji)

    """利用冒泡排序找出Chengji中的最大值最小值"""
    temp = ""
    for x in range(0,len(Chengji)-1):
        for y in range(0,len(Chengji)-x-1):
            if Chengji[y]>Chengji[y+1]:
                temp = Chengji[y]
                Chengji[y] = Chengji[y+1]
                Chengji[y+1] = temp
    print(Chengji)

    """第一个为最小值    最后一个为最大值      根据dic中键取值"""
    print(dic[str(Chengji[0])])
    print(dic[str(Chengji[-1])])

ChengjiSort()
