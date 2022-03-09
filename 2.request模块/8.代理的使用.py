"""
了解使用代理的过程
代理ip是一个ip, 指向的是一个代理服务器
代理服务器能够帮我们向目标服务器转发请求

将请求给代理, 然后由代理服务器转发给目标服务器

分类:
正向代理 反向代理
正向代理: 浏览器知道代理服务器是谁. VPN
反向代理: 浏览器不知道代理服务器谁代理. 不知道真实地址: nginx

代理ip(代理服务器)的分类
根据匿名程度:
    透明代理
    匿名代理
    高匿代理

毫无疑问使用高匿代理效果最好

协议:
    HTTP
    HTTPS
    socks



"""
import requests
# proxies代理服务器
# 直接设置给proxies参数

# 使用
# resp = requests.get(url, proxies=)
proxies = {
    "http":"http://ip",
    # ...
}
# 使用代理：
# https://www.kuaidaili.com/free/
# 使用代理, 成功不会有任何报错, 能成功获取W响应,
# 要么失败, 要么卡滞, 要么报错
url = "http://www.baidu.com"


proxies = {
    "http" : "http://12.127.123.12:80"
}
# 使用代理
resp = requests.get(url, proxies=proxies)

# 当你的ip被目标服务器封禁时候, 我们就可以使用代理进行转发
print(resp.text)





