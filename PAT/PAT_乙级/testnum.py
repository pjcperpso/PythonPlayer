"""python字符串截取"""
list = ["hEllo","Hello","Helo","hello","hell"]
str_test = "Hellohhelloooohlhello"
num = 0


#print(list[0].upper())
#for x in list:
    #if x.upper()=="HELLO":
        #num = num+1;
#print(num)

for i in range(0,len(str_test)):
    if str_test[i:i+5].lower() == "hello":
        num = num + 1;
print(num)
