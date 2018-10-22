"""求1/2+3/2+5/3+8/5+.....n"""
"""当前项的分子等于前一项的分子分母之和  当前项的分母等于前一项的分子"""
"""求前n项的和"""
def sum(i):
    fen_zi = 2
    fen_mu = 1
    temp = 0#临时变量
    sum = 0#第三方变量求和
    while True:
        sum+=fen_zi/fen_mu
        i = i-1
        if i==0:
            break
        temp = fen_zi+fen_mu
        fen_mu = fen_zi
        fen_zi = temp
    print(sum)

sum(3)
