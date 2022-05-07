"""
====================
Author:释法海
Time：2022/5/7 14:19
Porject：PYunittest
Address:shanghai
====================
"""
import re
from Common.handle_confing import conf
import  json
from Common.my_logger import logger


class  EnvData:
    """
    存储用例要使用的数据
    """
    pass
def clear_EnvData_attrs():
     # 清理EnvData里设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
         if key.startswith("__"):
             pass
         else:
             delattr(EnvData,key)

def replace_case_by_regular(case):
    """
    对Excel当中，读取出来的整条测试用例，做全部替换。
    包括url，request——data，expected，check_sql
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str):
            case[key] = replace_by_regular(value)
    logger.info("正则表达式替换完成之后的请求数据：\n{}".format(case))
    return case
def replace_by_regular(data):
    """
    将字符串当中，匹配#(.*?)#部分，替换对应的真实数据。
    真实数据只从2个地方去获取：1个是配置文件当中的data区域。另一个是，EnvData的类属性
    data：字符串
    return：返回的是替换后的字符串
    ps：1个是配置文件当中的data区域。另一个是，EnvData的类属性，必须是字符串类型
    """
    res = re.findall("#(.*?)#",data)
    if res:
        for item in res:
            try:
                value = conf.get("data",item)
            except:
                try:
                    value = getattr(EnvData, item)
                except AttributeError:
                    continue
            print(value)
            data = data.replace("#{}#".format(item),value)
    return data

def replace_mark_with_data(case,mark,real_data):
    """
    遍历一个http请求用例涉及到的所有数据，如果说每个数据有需要替换的，都会替换
    case：Excel当中读取出来的一条数据，是个字典
    mark：数据当中的占位符，#值#
    real_data：要替换mark的真实数据
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str):
            if value.find(mark) != -1:
                case[key] = value.replace(mark,real_data)
    return case


if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "http://api.lemonban.com/futureloan/#phone#/member/register",
        "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "美丽可爱的小简"}'
    }
    if case["request_data"].find("#phone#") != -1:
        case = replace_mark_with_data(case, "#phone#", "123456789001")
    for key,value in case.items():
        print(key,value)
