"""
====================
Author:释法海
Time：2022/5/7 17:47
Porject：PYunittest
Address:shanghai
====================
"""
import unittest
from jsonpath import jsonpath

import os
import json

from Common.handle_requests import send_requests
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.my_logger import logger
from Common.myddt import ddt,data
from Common.handle_data import replace_case_by_regular,EnvData,clear_EnvData_attrs
from Common.handle_extract_data_from_response import extract_data_from_response

# 读数据
he = HandleExcel(datas_dir + "\\api_cases.xlsx", "加标")
cases = he.read_all_datas()
he.close_file()

@ddt
class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("*************** 加标接口 开始测试 ***************")
        # 清理EnvData里设置的属性
        clear_EnvData_attrs()
        # 调用登录接口，获得token和member_id

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("*************** 加标接口 结束测试 ***************")

    @data(*cases)
    def test_add(self,case):
        # 替换case
        case = replace_case_by_regular(case)
        # 如果前置SQL - 得到结果后，再次替换
        # 发送请求 -考虑用例是否都需要token
        if hasattr(EnvData,"admin_token"):
            response = send_requests(case["method"],case["url"],case["request_data"],token=EnvData.admin_token)

        else:
            response = send_requests(case["method"], case["url"], case["request_data"])

        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],response.json())


