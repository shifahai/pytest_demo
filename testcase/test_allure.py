# coding=utf-8

import pytest
import allure

@allure.feature('测试用例')  # feature定义功能
class TestClass(object):

   @pytest.fixture(scope='function')
   def setup_function(request):
       def teardown_function():
           print("teardown_function called.")
       request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
       print('setup_function called.')

   @pytest.fixture(scope='module')
   def setup_module(request):
       def teardown_module():
           print("teardown_module called.")
       request.addfinalizer(teardown_module)
       print('setup_module called.')

   @allure.story('功能测试用例1')  # story定义用户场景
   @pytest.mark.website
   def test_1(setup_function):
       print('Test_1 called.')

   @allure.story('功能测试用例2')  # story定义用户场景
   def test_2(setup_module):
       print('Test_2 called.')

   @allure.story('功能测试用例3')  # story定义用户场景
   def test_3(setup_module):
       print('Test_3 called.')
       assert 2==1+1              # 通过assert断言确认测试结果是否符合预期

   @allure.story('功能测试用例4')  # story定义用户场景
   def test_4(setup_module):
       print('Test_4 called.')
       assert 3 == 1 + 1  # 通过assert断言确认测试结果是否符合预期
if __name__ == '__main__':
    pytest.main(["test_allure.py"])