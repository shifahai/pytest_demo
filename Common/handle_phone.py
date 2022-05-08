"""
====================
Author:释法海
Time：2022/5/7 17:20
Porject：PYunittest
Address:shanghai
====================
"""

# 1.数据生成11位手机号，前3位+8位
# 2.进行数据校验
import random
from Common.handle_db import HandleDB
from Common.handle_requests import send_requests

prefix = [133, 149, 153, 173, 177, 180, 181, 189, 199,
          130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186, 166,
          134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 198
          ]
# 获取新生成的手机号
def get_new_phoen():
    db = HandleDB()
    while True:
        # 1.生成手机号
        phoen = __generator_phoen()
        # 2.校验，在数据库中是否有
        count = db.get_count('select * from member where mobile_phone="{}"'.format(phoen))
        if count == 0: #如果手机号吗没有在数据库查到。表示是未注册的号码
            db.close()
            return phoen

def get_old_phone():
    """
    从配置文件获取指定用户名和密码
    确保此账号，在系统当中是注册了的
    :return: 返回用户名密码
    """
    from Common.handle_confing import conf
    user = conf.get("general_user","user")
    passwd = conf.get("general_user","passwd")
    send_requests("POST","member/register",{"mobile_phone":user,"pwd":passwd})
    return user,passwd

# 封装生成手机号
def __generator_phoen():
    index = random.randint(0,len(prefix)-1)
    phoen = str(prefix[index])
    for _ in range(0,8):
        phoen +=str(random.randint(0,9))
    return phoen


print(get_old_phone())