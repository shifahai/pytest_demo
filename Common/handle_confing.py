"""
====================
Author:释法海
Time：2022/5/6 19:53
Porject：PYunittest
Address:shanghai
====================
"""
from configparser import ConfigParser
import os
from Common.handle_path import conf_dir

class  HandleConfig(ConfigParser):
    def __init__(self,file_path):
        super().__init__()
        self.read(file_path,encoding="utf-8")

file_path = os.path.join(conf_dir,"nmb.ini")
conf = HandleConfig(file_path)

if __name__ == '__main__':
    file_path = os.path.join(conf_dir, "nmb.ini")
    conf = HandleConfig(file_path)
    print(conf.get("mysql","port"))