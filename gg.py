#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

import xlwt
from sshtunnel import SSHTunnelForwarder #ssh连接
with SSHTunnelForwarder(
        ('112.25.69.61', 22),  # B机器的配置
        ssh_password="NJXJ^1jsyd",
        ssh_username="local",
        remote_bind_address=('localhost', 21605)) as server:  # A机器的配置,数据库IP，端口
    print(2)#测试
    con = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                          port=server.local_bind_port,
                          user='xjgame',  # 数据库用户
                          passwd='XJgame025133',  # 数据库密码
                          db='base_log_db')  # 库名
    print(1)#测试
    cur = con.cursor(cursor=pymysql.cursors.DictCursor)  # 游标设置为字典类型，便于获取数据
    sql = ("SELECT COUNT( USER_ID ) 点击数（PV）,COUNT( DISTINCT USER_ID ) 点击人数（UV）,APK_VERSION APK版本,MODULE_NAME 产品名（1xldm，2xjly，3lwt，4xmcb，5xhbly，6少儿频道）,substr( CREATE_DATE, 1, 10 ) 时间 "
            "FROM`njxj_log_common_page_tab`"
            "WHERE city_name LIKE '%江苏%'"
            "AND USER_NET_TYPE='1'"
            "AND MODULE_NAME = '3'"
            "AND substr( CREATE_DATE, 1, 10 ) between '2020041100' AND '2020041108')")
    print(sql)#测试
    cur.execute(sql)

    # 获取多条查询数据
    ret = cur.fetchall()
    print(3)#测试
    for file in ret:
        print(file)
        print('-' * 10)
cur.close()
con.close() #关闭连接
