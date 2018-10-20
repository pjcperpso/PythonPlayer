import cx_Oracle
import re
"""曲先森"""
"""使用正则表达式    判断注册账号是否合法     规定账号格式"""
em = re.compile(r'[a-zA-Z0-9]{6,10}@(163|126|qq|sina).com$')
"""登录功能"""
def login():
    """和数据库创建连接1"""
    db = cx_Oracle.connect('用户名/密码@ip地址:端口号')
    cursor = db.cursor()
    flag = 1
    m = input("please input your loginname:")
    n = input("please input your loginpsw:")
    try:
        """判断用户名和密码是否正确"""
        x = cursor.execute("select name,passwd from users")
        for i in x:
            """print(type(i)) i为元组类型"""
            print(type(i))
            if i[0]==m and i[1]==n:
                print("登陆成功")
                flag = 0
        if flag:
            print("登录失败")
    except cx_Oracle.DatabaseError as e:
        print(e)
    """关闭连接"""
    cursor.close()
    db.close()



"""注册"""
def register():
    db = cx_Oracle.connect('用户名/密码@ip地址:端口号')
    cursor = db.cursor()
    """循环注册操作"""
    while True:
        flag = input("请问是否注册(yes/no):")
        if flag == 'yes':
            m = input("please input your registername:")
            if em.match(m):
                username = em.match(m)
                n = input("please input your registerpsw:")
                insert_sql = "insert into users values('"+username.group()+"','"+n+"')"
                try:
                    cursor.execute(insert_sql)
                    print(cursor.rowcount)
                    db.commit()
                except cx_Oracle.DatabaseError as e:
                    print(e)
                    db.rollback()
                cursor.close()
                db.close()
            else:
                print("用户名不合法")
        if flag == 'no':
            return


register()
login()
