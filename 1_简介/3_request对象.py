from urllib.request import urlopen
from urllib.request import Request
# 我们需要设置UA. 即用户标识信息, 这也是经常使用的
import random
from random import choice

# 随机创建UA, 的专用模块.
# from fake_useragent import UserAgent

url = "https://www.baidu.com"

# 设置动态UA: 每次请求时不同.
# 百度一下UA, 可以准备多个UA
UA_list = [ # 只放UA的value, 后面会进行拼接.
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
]

print(choice(UA_list)) # 每次随机从列表中取一个数据

headers = {
    "User-Agent": random.choice(UA_list)
}



# 静态
# headers = { # 从开发者工具, 或者fiddler中抓包.
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
# }
request = Request(url, headers=headers) # 使用Request进行创建请求对象
print(request.get_header('User-agent')) # 只有只这样才能获取UA, 原因是headers传入的时候做处理了.

response = urlopen(request) # 传入请求 -> request, 返回response(响应)

info = response.read()

print(info.decode())

