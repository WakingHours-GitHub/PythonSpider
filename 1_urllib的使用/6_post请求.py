"""
post请求:
隐式传参, 也就是额外传输一个参数, 用于放置参数.
常在登录页面中看到POST请求.

    Request请求对象中有data参数, 他就是在post里的的参数,
    data是一个字典, 需要匹配键值对
使用POST请求:
    Request(url, data=data)
    传入data参数, 注意是字节. 所以我们需要使用urlencode()进行转换. 然后使用encode()进行转换bytes


过程:
    字典 -> str(使用urlencode()) -> bytes

"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

url = 'http://www.sxt.cn/index/login/login.html'
headers = {
    'user-agent': UserAgent().random
}

# 创建字典
form_data = {
    'user': '17703181473',
    'password': '123456'
}

# 转换字符串:
f_data = urlencode(form_data)
print(f_data.encode()) # b'user=17703181473&password=123456' #  转换为字节形式.

# 封装请求头
request = Request(url, headers=headers, data=f_data.encode())

# 发送请求
response = urlopen(request)

print(response.read().decode())



