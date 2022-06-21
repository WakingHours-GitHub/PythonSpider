import requests
# 发送带headers的请求
# requests.get(url,headers={}) headers参数接收字典形式的请求头
# UserAgent 可以通过浏览器抓包来获取

url = "http://www.baidu.com"

# 构建请求头字典
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
}
# 发送带请求头的请求
resp1 = requests.get(url,headers=headers)

print(resp1.text)
# 这样就已经做了一层伪装了, 就是标志你是一个浏览器


# 发送带参数的请求
# 在使用浏览器时, 我们常常会发现url地址中有一个?, 那么?后面就是请求参数, 又叫做查询字符串
# 然后我们需要判断什么是关键参数, 这很简单, 我们只需要, 再地址栏中挨个删除, 看删除那个后, 得到的结果和之前不一样了, 就说明这个是关键参数

# 发送带参数的请求有两种方式:
# 1. url中直接带有参数
# 2. 通过params携带参数字典

# https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0x870e136b0009f01f&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&rsv_sug3=7&rsv_sug2=0&rsv_btype=i&inputT=1119&rsv_sug4=1807
# https://www.baidu.com/s?wd=python
# 1. url中直接带有参数 -> 简单粗暴.
url = "https://www.baidu.com/s?wd=python"
resp2 = requests.get(url, headers=headers)

with open("baidu1.html", "wb") as f: # 以二进制的方式写入
    f.write(resp2.content) # 写入字节文件

# 2. 通过params携带参数字典.
url = "https://www.baidu.com/s?"
params = {
    "wd": "python"
}

resp3 = requests.get(url, headers=headers, params=params)

print(resp3.url) # https://www.baidu.com/s?wd=python

with open("baidu2.html", "wb") as f:
    f.write(resp3.content)





