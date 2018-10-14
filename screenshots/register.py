#coding=utf-8

import MySQLdb
from login_page import *
from Tkinter import *
from tkMessageBox import *
from tkFont import Font
import string


class loginPage(object):
    def __init__(self, master, info=u'欢迎您进入注册页面'):
        self.master = master
        self.master.title(u'注册')
        self.mainlabel = Label(master, text=info, justify=CENTER)
        self.mainlabel.grid(row=0, columnspan=3)

        self.user = Label(master, text=u'注册用户名：', borderwidth=3)
        self.user.grid(row=1, sticky=W)

        self.pwd = Label(master, text=u'注册密码：', borderwidth=3)
        self.pwd.grid(row=2, sticky=W)

        self.userEntry = Entry(master)
        self.userEntry.grid(row=1, column=1, columnspan=3)
        self.userEntry.focus_set()

        self.pwdEntry = Entry(master, show='*')
        self.pwdEntry.grid(row=2, column=1, columnspan=3)

        self.loginButton = Button(master, text=u'注册', borderwidth=2, command=self.login)
        self.loginButton.grid(row=3, column=1)

        self.clearButton = Button(master, text=u'返回', borderwidth=2, command=self.clear)
        self.clearButton.grid(row=3, column=2)

    def login(self):
        self.username = self.userEntry.get().strip()
        self.passwd = self.pwdEntry.get().strip()
        
        txt = u'''用户名: %s \n密码  : %s ''' % (self.userEntry.get(), self.pwdEntry.get())
        # 打开数据库连接
        db = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="chat", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        # sql = "INSERT INTO user(username, password) VALUES ('%s', '%s')" % (self.username, self.passwd)
        sql = "INSERT INTO user VALUES ('%s', '%s', 0)" % (self.username, self.passwd)
        # cursor.execute(sql)
        # showinfo('注册成功！！！', txt)
        # print
        # "数据插入成功！！！".decode("utf-8").encode("gb2312")
        # # 提交到数据库执行
        # db.commit()
        try:
            # 执行sql语句
            cursor.execute(sql)
            showinfo('注册成功！！！', txt)
            print "数据插入成功！！！".decode("utf-8").encode("gb2312")
            # 提交到数据库执行
            db.commit()
        except:
            print "数据插入失败！！！".decode("utf-8").encode("gb2312")
            # Rollback in case there is any error
            db.rollback()

        # 关闭数据库连接
        db.close()



    def clear(self):
        self.userEntry.delete(0, END)
        self.pwdEntry.delete(0, END)
        Login()
        
if __name__ == '__main__':
    root = Tk()
    myLogin = loginPage(root)

    # root.wait_window(myLogin.mySendMail.sendPage)
    mainloop()