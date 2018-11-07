biaozhun = "60 80"
stu = ['1000 100 120','1001 20 30','1002 88 66','1005 88 92','1006 66 70','1007 88 99','1008 99 99','1009 66 66','1010 102 120']
message = biaozhun.split(" ")
"""分类讨论"""
"""德才均大于80"""
"""德大于80 才小于80"""
"""德才均小于80"""
dictgood = {}
dictliang = {}
dictcha = {}
Lgood = []
Lliang = []
Lcha = []
for x in stu:
    one = x.split(" ")
    if(one[1]>=message[0] and one[2]>=message[0]):

        if one[1]>=message[1] and one[2]>=message[1]:
            all = int(one[1])+int(one[2])
            dictgood[all] = x
            Lgood.append(all)
        elif one[1]>=message[1] and one[2]<message[1]:
            allliang = int(one[1])+int(one[2])
            dictliang[all] = x
            Lliang.append(allliang)
        elif one[1]<message[1] and one[2]<message[1]:
            allcha = int(one[1])+int(one[2])
            dictcha[all] = x
            Lcha.append(allcha)
def sort(L):
    temp = 0
    for x in range(0,len(L)-1):
        if L[x]>L[x+1]:
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
    return L

def out(L,dict):
    for x in L:
        print(x,dict[x])
