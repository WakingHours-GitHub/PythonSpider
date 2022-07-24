"""
opener的使用:

# 可以请求: 下面的URL: 通过请求该URL, 返回你请求的信息.
    你的headers信息: 包括你的UA信息, 你的ip/
    http://httpbin.org/get

"""

from urllib.request import Request
from urllib.request import build_opener

from urllib.request import HTTPHandler
from urllib.request import ProxyHandler

from fake_useragent import UserAgent

# url = "https://www.baidu.com"
url = "http://httpbin.org/get"

headers = {
    'user-agent': UserAgent().chrome
}

request = Request(url, headers=headers)

# 查看urlopen()源码, 发现其中就是使用opener对象发送请求的.
# 使用build_opener()构建opener对象
# build_opener()时候可以传入一个Handler对象, 如果我们想要设置代理的话, 就在这里设置
# handler = HTTPHandler() # 普通的http请求.

# 设置代理:
# ProxyHandler({"传输协议": "username:password@ip:port"})
# ProxyHandler({"传输协议": "ip:port"})


handler = ProxyHandler( # 传入一个字典, 用于表示什么请求方式, 和ip以及端口
    {
        "http": "111.42.175.236:9091" #
    },
    # { # 如果是使用购买的ip代理:
        # 则使用下面的方式:
        # '请求': user:passwd@ip:part

    # }
)
opener = build_opener(handler)
# response = opener.open(request)

response = opener.open(request) # urlopen()源码也是使用opener发送请求的。

print(response.read().decode()) #

# "origin": "111.42.175.236", # 可见, 代理已经生效了.