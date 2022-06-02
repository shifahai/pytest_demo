# Pytest+requests+allure+excel+log+mail+配置文件接口自动化测试框架
## 一、目录结构
```
│  readme.md
│  requirements.txt
│  run.py            
├─case
│  │  test_case_encapsulation.py # 测试方法
│  │  case_result_assert.py # 封装断言方法
│          
├─common # 公共方法
│  │  connect_data.py # 数据库连接封装
│  │  get_cookie.py # 获取环境cookie封装
│  │  case_filepath.py # 获取测试用例路径
│  │  readcasedata.py # 读取测试用例数据封装
│  │  readConfig.py # 读取配置封装
│  │  send_mail_result.py # 邮件发送封装
│  │  zip_result.py # 压缩文件封装
│          
├─config # 配置环境
│      conf.ini # 环境配置
│      log.ini # 日志配置
│      mail.ini # 邮件配置
│      
├─data # 测试用例
│      data.xls # 测试用例
│      
├─log # 日志文件
│  │  record_log.py # 日志方法封装
│          
└─report # 测试报告
```
## 二、环境配置
+ 使用时，在终端使用```pip install -r requirements.txt```
```
allure-pytest==2.9.45
allure-python-commons==2.9.45
async-generator==1.10
atomicwrites==1.4.0
attrs==21.4.0
beautifulsoup4==4.11.1
certifi==2021.10.8
cffi==1.15.0
charset-normalizer==2.0.12
click==8.1.3
colorama==0.4.4
cryptography==37.0.2
cssselect==1.1.0
demjson==2.2.4
Flask==2.1.2
freegames==2.4.0
h11==0.13.0
idna==3.3
importlib-metadata==4.11.3
iniconfig==1.1.1
itsdangerous==2.1.2
Jinja2==3.1.2
jsonpath==0.82
lxml==4.8.0
MarkupSafe==2.1.1
mysqlclient==2.1.0
outcome==1.1.0
packaging==21.3
pluggy==1.0.0
py==1.11.0
pycparser==2.21
PyMySQL==1.0.2
pyOpenSSL==22.0.0
pyparsing==3.0.8
pyquery==1.4.3
PySocks==1.7.1
pytest==7.1.2
pytest-assume==2.4.3
pytest-html==3.1.1
pytest-metadata==2.0.1
requests==2.27.1
selenium==4.1.5
six==1.16.0
sniffio==1.2.0
sortedcontainers==2.4.0
soupsieve==2.3.2.post1
tomli==2.0.1
trio==0.20.0
trio-websocket==0.9.2
typing_extensions==4.2.0
urllib3==1.26.9
Werkzeug==2.1.2
wsproto==1.1.0
xlrd==2.0.1
XlsxWriter==3.0.3
xlutils==2.0.0
xlwt==1.3.0
zipp==3.8.0
```
## 三、使用介绍
### 3.1 配置环境

### 3.2 测试用例维护
### 3.3 测试方法介绍
### 3.4 断言方法封装
### 3.5 日志介绍
### 3.6 调用
运行主程序即可