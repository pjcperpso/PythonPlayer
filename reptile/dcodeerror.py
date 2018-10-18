from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import cx_Oracle

"""采集部分香港90年代电影信息  调用相关函数进行入库"""
def gather_data():
    for i in range(1,6):
        url = "http://list.iqiyi.com/www/1/28997-----------1990_1999--11-"+str(i)+"-1-iqiyi--.html"
        """爬取网页数据  html数据采集"""
        html_date = urlopen(url).read().decode('utf-8')
        """bs解析  bs标准库解析"""
        bs_html = bs(html_date,'html.parser')
        """获取相关数据  获取html标签为a，元素rseat=bigTitle的所有内容"""
        all_list = bs_html.findAll('a',rseat='bigTitle')
        for one in all_list:
            getconn(one.get_text(),one.get('href'))


"""链接数据库、进行入库操作"""
def getconn(a,b):
    conn = cx_Oracle.connect('admin/admin@localhost:1521')
    cursor = conn.cursor()
    sql = "insert into movie values('"+a+"','"+b+"')"
    try:
        cursor.execute(sql)
        print(cursor.rowcount)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

gather_data()
