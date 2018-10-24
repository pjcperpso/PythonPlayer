"""冒泡排序 Maopao"""
def Maopao():
    L = [1000,5,4,3,9,8,21000]
    #临时存储变量
    temp = 0
    #单次排序
    for x in range(1,len(L)):
        #每次排序要比较的次数
        for y in range(1,len(L)-x+1):
            #如果后面的元素>前面的元素  则替换
            if L[-y]>L[-y-1]:
                temp = L[-y]
                L[-y] = L[-y-1]
                L[-y-1] = temp
        print(L)

Maopao()
