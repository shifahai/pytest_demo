"""
====================
Author:释法海
Time：2022/6/1 22:06
Porject：Pytest_demo
Address:shanghai
====================
"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试用例路径
cases_dir = os.path.join(base_dir, "testcase")
# 测试用例调试路径
debug_dir = os.path.join(base_dir, "testdebug")
# 测试数据的路径
data_dir = os.path.join(base_dir, "data")
# 测试报告的路径
reports_dir = os.path.join(base_dir, "report")
# 日志的路径
logs_dir = os.path.join(base_dir, "logs")
# 配置文件路径
config_dir = os.path.join(base_dir, "config")
