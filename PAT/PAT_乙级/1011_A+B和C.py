"""给出任意三个数
   判断A+B是否>C
"""
num = input("please input num:")
right = []
for x in range(0,int(num)):
    message = input("请给出A、B和C(以空格分开):")
    list_message = message.split(" ")
    if int(list_message[0])+int(list_message[1])>int(list_message[2]):
        right.append("true")
    else:
        right.append("false")
        print(list_message[0],list_message[1],list_message[2])
for x in range(0,int(num)):
    print("Case #",x,":",right[x])
