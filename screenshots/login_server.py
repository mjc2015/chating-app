#coding:utf-8

import json,time
import subprocess
import MySQLdb
import socket


    #class MyServer(object):
 #       def handle(self):
ip_port = ('127.0.0.1',9999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ip_port)
s.listen(5)
while True:
            
            conn, addr = s.accept()
            print 'Connected from', addr
            while True:
                data = conn.recv(1024)
                
                if not data:
                    break
                else:
                    dataobj = json.loads(data.decode('utf-8'))
                    
                    print dataobj
                
                en1_value = dataobj[0]
                en2_value = dataobj[1]
    
                db = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="chat", charset="utf8")
                # 使用cursor()方法获取操作游标
                cursor = db.cursor()
                # SQL 查询语句
                sql = "select * from user"
                
                ret = '1'
                try:
                    # 执行SQL语句
                    cursor.execute(sql)
                    # 获取所有记录列表
                    results = cursor.fetchall()
                    for row in results:
                        name = row[0]
                        pwd = row[1]
                        if name == en1_value and pwd == en2_value:
                            print "数据库连接及验证成功！！！".decode("utf-8").encode("gb2312")
                            ret = '0'
                    # # 打印结果
                except:
                    print "Error: unable to fecth data"
                     
            # 关闭数据库连接
                db.close()
                conn.send(ret.encode('utf-8'))
#conn.close()
    
'''if __name__ == '__main__':
    MyServer.handle()
    print('Waiting for connection....')'''