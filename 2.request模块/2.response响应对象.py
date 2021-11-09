import requests

url = "http://www.baidu.com"

response = requests.get(url)
# 手动设定编码格式
response.encoding = "utf8"  # 设置字符集

print(response.text)
# response.text都是requests模块按照chardet模块推测的编码字符集进行解码的结果
# 网络上传输的字符串都是bytes类型的, 所以response.test = response.content.decode()
# 再网页中
print(response.encoding)  # ISO-8859-1 utf8

# 第二种方式
# response.content是存储的bytes类型的响应源码 可以进行decode操作
print(response.content)  # xe6\x84\x8f\xe8\xa7\x81\xe5\x8f\x8d\xe9\xa6\x88<
print(response.content.decode())  # 也可以正确打印出来结果
# response.content.decode() # 默认解码是utf8

# response响应对象的其他常用属性或方法:
# response.url 响应的url; 有时候响应的url和请求的url并不一致
# response.status_code 响应状态码, 正常是200
# response.request.headers 响应对应的请求头
# response.headers 响应头
# response.request.cookies 响应对应请求的cookie; 返回cookieJar类型
# respose.json() 自动将json字符串类型的响应内容转换为python对象(dict 或 list)

# 响应url
print(response.url)

# 状态码
print(response.status_code)

# 响应对应的请求头 -> 请求头
print(response.request.headers)

# 响应头
print(response.headers)

# 响应设置cookies
print(response.cookies)

