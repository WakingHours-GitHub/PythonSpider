# requests这个http模块
# 该模块主要用于发送请求, 获取响应
# 比urllib代码间接
# 接下来开始学习request模块

"""
本章节知识点:
- 掌握headers参数的使用
- 掌握发送带参数的请求
- 掌握headers中携带cookie
- 掌握cookies参数的使用
- 掌握cookieJar的转换方法
- 掌握超市参数timeout的使用
- 掌握代理ip参数proxies的使用
- 掌握verify参数忽略CA整数
- 掌握requests模块发送post请求
- 掌握利用requests.session进行状态保持

"""
""" 
1. requests介绍
    1.1 requests模块的作用:
        发送http请求, 获取响应数据
    1.2 requests安装
        pip install requests
    1.3 requests模块发送get请求
        导入模块
        使用get方法, 对url发送请求
"""

import requests

url = "http://baidu.com"

response = requests.get(url)

# 打印源码的str类型数据
print(response.text)