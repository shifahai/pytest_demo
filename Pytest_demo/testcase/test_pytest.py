# -*- coding: UTF-8 -*-
import pytest


# 1.规定：
# 测试文件以test_开头（以_test结尾也可以）
# 测试类以Test开头，并且不能带有 init 方法
# 测试函数以test_开头
# 断言使用基本的assert即可
# 2.执行模块命令：
# pytest 模块名称 例如：pytest test_123.py

# 3.生成测试报告
# pytest --html=report.html

# 4.运行模式
# 模式1：直接运行test_hello.py文件中的所有cases: pytest test_hello.py
# 模式2：运行test_hello.py文件中的TestClassOne这个class下的两个cases: pytest test_hello.py::TestClassOne
# 模式3：运行test_hello.py文件中的TestClassTwo这个class下的test_one: pytest test_hello.py::TestClassTwo::test_one
class TestClassOne(object):
    def test_one(self):
        x = "this"
        assert 't' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'hello')== "False"



class TestClassTwo(object):
    def test_one(self):
        x = "iphone"
        assert 'p' in x

    def test_two(self):
        x = "apple"
        assert hasattr(x, 'check')







