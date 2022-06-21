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
于是我们登录 -> 保存日志
然后在session中, 看到一个重定向 -> 登录页面
发现post的data中也有这个什么什么token
然后我们从新开一个虚拟窗口, 再次登录.
发现这个token是不一样的, 所以token是变化的.
然后我们看看他是怎么来的,
从html(文档document) -> js -> css 检查哪里有这个token的生成
ctrl + shift + f 全局搜索, ctrl + f 搜索
检查可以发现, 在login中可以找到 这串token的生成 -> 这也我们就能获取它了
如何获取? -> 简单:
    对login发送请求, 在响应中正则这个token值就可以了

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

    # authenticity_token: nbToeJLMBQXOmO/+8jrbzdhaA8/z/XAmz9F5lICV98YES21NVWjYX+VxUu1irMtGsP4LT4F8TslD0z29HP8wFQ==
    # 获取token的url -> 我们需要请求这个url然后利用正则进行匹配
    get_token_url = "https://github.com/login"
    get_token_resp = session.get(get_token_url, timeout=3)
    print(type(get_token_resp.content.decode()))

    # 然后利用正则进行匹配
    token = re.findall('name="authenticity_token" value="(.*?)" />', get_token_resp.content.decode())[0]
    print(token) # 成功获取这个token

    # 然后我们需要带着这个url去登录 -> 访问/session
    url2 = "https://github.com/session"
    data = {
        "commit": "Sign in",
        "authenticity_token":token, # 换上我们刚才获取的token
        "login": "WakingHours - GitHub",
        "password": "FWJ@15246337585",
        "return_to": "https: // github.com /login".replace(" ", "")
    }
    # 登录 -> 然后这个session就会自动处理cookie
    session.post(url2, data) # session请求, 这个url2, 并且自动处理cookie

    # 验证
    url3 = "https://github.com/WakingHours-GitHub"
    resp3 = session.get(url3)

    with open("github.html", "wb") as f:
        f.write(resp3.content)

    # 看title标签中的内容, 证明登录成功




if __name__ == '__main__':
    login()