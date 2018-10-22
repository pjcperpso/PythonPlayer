from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
num = [0,0,0,0,0,0,0]
"""采集数据 90年代香港电影各大知名影星影视作品数量"""
def names_num():
    for x in (range(1,27)):
        url = "http://list.youku.com/category/show/c_96_a_%E4%B8%AD%E5%9B%BD%E9%A6%99%E6%B8%AF_r_1990_s_1_d_1_p_"+str(x)+".html?spm=a2h1n.8251845.0.0"
        html_parse = urlopen(url).read().decode('utf-8')
        soup = bs(html_parse,'html.parser')
        all_message = soup.findAll('li',{'class':'actor'})
        for one in all_message:
            names = one.get_text()
            if '周星驰' in names:
                num[0] = num[0]+1
            if '张国荣' in names:
                num[1] = num[1]+1
            if '张曼玉' in names:
                num[2] = num[2]+1
            if '王祖贤' in names:
                num[3] = num[3]+1
            if '成龙' in names:
                num[4] = num[4]+1
            if '刘德华' in names:
                num[5] = num[5]+1
            if '张学友' in names:
                num[6] = num[6]+1
    return num
"""绘制图形表明"""
import matplotlib.pyplot as plt
def draw():
    nums = names_num()
    print(nums)
    names = ['Xing_chi','Guo_rong','Man_yu','Zu_xian','Cheng_long','De_hua','Xue_you']
    #plt.plot(names,nums,linewidth=2)
    plt.scatter(names,nums,s=5)
    plt.show()

draw()
