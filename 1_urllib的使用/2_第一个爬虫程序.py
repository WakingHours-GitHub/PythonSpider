import urllib
from urllib.request import urlopen # 用于向URL发送请求
# urlopen(url)

# 发送请求
url = "https://www.baidu.com"
response = urlopen(url)




# 读取内容
info = response.read()

print(info.decode())

response.close()


# 打印状态码:
print(response.getcode()) # 返回HTTP的响应码， 成功为200, 4开头为服务器页面出错, 5为服务器错误

# 打印真实url
print(response.geturl())

# 打印响应头
print(response.info())


