"""
给定两个数值根据时间戳求时间
"""

#格式  hh:mm:ss
#四舍五入  暴力取整
import math
def getTime():
    i = 4577973-123
    #取小时
    h = i//(100*3600)
    #取分钟
    m = int(i/100%3600/60)
    #取秒
    s = int(i/100%3600%60+0.5)
    print(h,":",m,":",s)
getTime()
