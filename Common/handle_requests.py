"""
====================
Author:释法海
Time：2022/5/7 15:33
Porject：PYunittest
Address:shanghai
====================
"""
import requests
import json
from Common.my_logger import logger
from Common.handle_confing import conf


def send_requests(method, url, data=None, token=None):
    logger.info("发送一次Http请求")
    headers = __handle_header(token)
    url = __pre_url(url)
    data = __pre_data(data)
    logger.info("请求头为： {}".format(headers))
    logger.info("请求方法为： {}".format(method))
    logger.info("请求url为： {}".format(url))
    logger.info("请求数据为： {}".format(data))
    method = method.upper()
    if method == "GET":
        resp = requests.get(url, data, headers=headers)
    else:
        resp = requests.post(url, json=data, headers=headers)
    logger.info("响应状态码为： {}".format(resp.status_code))
    logger.info("响应数据为： {}".format(resp.json()))
    return resp


def __handle_header(token=None):
    """
    处理请求头。加上项目党总必带的请求头，如果有token，加上token
    :param token:token值
    :return:处理后的headers字典
    """
    headers = {"X-Lemonban-Media-Type": "lemonban.v2",
               "Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers


def __pre_url(url):
    """
    拼接接口的URL地址
    """
    base_url = conf.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + "/" + url


def __pre_data(data):
    """
    如果data是字符串，则转换成字典对象
    :param data:
    :return:
    """
    if data is not None and isinstance(data, str):
        if data.find("null") != -1:
            data = data.replace("null", "None")
        data = eval(data)
    return data
