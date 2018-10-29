x = input("please input this num:")
list_x = x.split(" ")
if len(list_x[0])==4:
    print(int(int(list_x[0])/100),int(list_x[0])%100)
