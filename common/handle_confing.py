"""
====================
Author:释法海
Time：2022/6/2 13:06
Porject：PytestProjects
Address:shanghai
====================
"""
import configparser
import os
from common.handle_path import config_dir

class HandleConfig():
    """
    此类用于读取配置文件的操作封装
    """
    def __init__(self,locator):
        self.locator = locator
        file_path = os.path.join(config_dir,self.locator)
        self.conf = configparser.ConfigParser()
        self.conf.read(file_path,encoding="utf-8")

    # 读取测试环境地址
    def read_test_evn(self,emo):
        test_evn = self.conf.get('server',emo)
        return test_evn

    # 读取日志配置
    def read_logs_conf(self, msg):
        logs_conf = self.conf.get('log', msg)
        return logs_conf

    # 读取测试账号信息
    def read_user_conf(self,msg):
        user_conf = self.conf.get('general_user',msg)
        return user_conf

    # 读取数据库信息
    def read_db_conf(self,msg):
        db_conf = self.conf.get('mysql',msg)
        return db_conf

    # 读取邮箱信息
    def read_mail_conf(self,tp):
        mail_conf = self.conf.get('MAIL',tp)
        return mail_conf

    # 读取测试登录信息
    def read_data_conf(self,tp):
        data_conf = self.conf.get('data', tp)
        return data_conf





