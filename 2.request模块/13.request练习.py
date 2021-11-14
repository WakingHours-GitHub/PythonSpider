"""
利用session进行状态保持

登录github.com
并进行状态保持
# 真正进行分析cookie过程

# 看整个登录, 其实是一个表单域
<form action="/session" accept-charset="UTF-8" method="post">
action是点击后, 这个表单域会到哪里去
method就是发送的方式
发现有一个<input> 中有什么什么token

"""
import requests
import re

# 进行
def login():
    session = requests.session() # 实例化session对象
    # headers可以有两种方式添加
    # session.headers = {}
    # session.get(headers)
    session.headers = { # session设置headers
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
    }



