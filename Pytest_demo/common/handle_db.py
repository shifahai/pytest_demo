"""
====================
Author:释法海
Time：2022/6/2 12:53
Porject：PytestProjects
Address:shanghai
====================
"""
import pymysql

from common.handle_confing import HandleConfig


class HandleDB:

    def __init__(self):
        rd = HandleConfig('conf.ini')
        # 连接数据库，创建游标
        # 1.建立链接
        self.conn = pymysql.connect(
            host=rd.read_db_conf('host'),
            port=rd.read_db_conf('port'),
            user=rd.read_db_conf('user'),
            password=rd.read_db_conf('password'),
            database=rd.read_db_conf('database'),
            charset=rd.read_db_conf('charset'),
            cursorclass=pymysql.cursors.DictCursor
        )
        # 2.创建游标
        self.cur = self.conn.cursor()

    # 查询单个数据
    def select_one_data(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    # 查询单个数据
    def select_all_data(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    # 获取数量
    def get_count(self, sql):
        self.conn.commit()
        return self.cur.execute(sql)

    # 对数据进行增删改操作
    def update(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        self.cur.close()
        self.conn.close()


