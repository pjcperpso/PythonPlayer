filename = 'question.txt'
with open(filename,'r',encoding='UTF-8') as text:
    right_num = 0.0
    sum = 0.0
    title = input("请问是否准备答题?(yes/no)?")
    if title == 'yes':
        for one in text:
            sum = sum+1
            message = one.rstrip().split("|")
            print(message[0]+"  "+message[1]+"  "+message[2]+"  "+message[3]+"  "+message[4])
            response = input("请输入答案:")
            if response!='A' and response!='B' and response!='C' and response!='D':
                response = input("输入有误,请重新输入答案:")
            else:
                if response == message[5]:
                    right_num = right_num+1


print("本次您答对了",right_num,"道题,正确率为",right_num/sum)
