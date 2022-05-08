"""
====================
Author:释法海
Time：2022/5/8 11:29
Porject：PYunittest
Address:shanghai
====================
"""
import unittest
import os
import json

from Common.handle_requests import send_requests
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.handle_db import HandleDB
from Common.my_logger import logger
from Common.myddt import ddt,data
from Common.handle_phone import get_new_phoen
from Common.handle_data import replace_mark_with_data

he = HandleExcel(datas_dir,"\\api_cases.xlsx","注册")
cases = he.read_all_datas()
he.close_file()

db = HandleDB()

@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("=========== 注册模块用例 开始执行 ============")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("=========== 注册模块用例 执行结束 ============")

    @data(*cases)
    def test_register(self,case):
        logger.info("*************** 执行用例{}: {} ****************".format(case["id"],case["title"]))

        # 替换 - 动态
        # 请求数据#phone# 替换 new_phone
        # checl_sql 里的 #phone# 替换 new_phone
        if case["request_data"].find("#phone#") != -1:
            new_phone = get_new_phoen()
            case = replace_mark_with_data(case,"#phone#",new_phone)

        # 步骤测试数据 - 发起请求
        response = send_requests(case["method"],case["url"],case["request_data"])
        #期望结果，从字符串转换成字典对象
        expected = eval(case["expected"])
        # 断言 - code ==0 msg ==ok
        logger.info("用例的期望结果为：{}".format(case["expected"]))
        try:
            self.assertEqual(response.json()["code"],expected["code"])
            self.assertEqual(response.json()["msg"], expected["msg"])
            # 如果check_sql有值，说明要做数据库校验。
            if case["check_sql"]:
                # logger.info()
                result = db.select_one_data(case["check_sql"])
                self.assertIsNotNone(result)
        except AssertionError:
            logger.exception("断言失败！")
            raise

