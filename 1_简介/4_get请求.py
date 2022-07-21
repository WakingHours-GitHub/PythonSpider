"""
get请求: 显示请求, URL ?后面加上参数: key=value, 使用&分割参数.
post请求: 隐式请求.






"""
from fake_useragent import UserAgent
from urllib.request import urlopen, Request
# 中文字符串编码:
from urllib.parse import quote, urlencode


headers = {
    'User-Agent': UserAgent().random
}

# 转换中文编码

# 使用quote
print(quote("尚硅谷")) # %E5%B0%9A%E7%A1%85%E8%B0%B7 # 进行转码
# 然后我们拼接到URL中即可
url = "https://www.baidu.com/s?wd={}".format(quote("尚硅谷"))

# 使用urlencode
args = {
    'wd': "尚硅谷",
    'ie': "utf-8"
}
print(urlencode(args)) #wd=%E5%B0%9A%E7%A1%85%E8%B0%B7&ie=utf-8 # 直接将多个参数拼接

url = "https://www.baidu.com/s?{}".format(urlencode(args))
# 直接在?后面拼接参数即可.


request = Request(url, headers=headers)
response = urlopen(request)
info = response.read()
print(info.decode()) #


