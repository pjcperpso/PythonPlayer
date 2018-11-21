xx = '6435'
temp = 0
x = list(xx)
for z in range(0,len(x)-1):
    if x[z]>x[z+1]:
        temp = x[z]
        x[z] = x[z+1]
        x[z+1] = temp
print("".join(x))
