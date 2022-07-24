from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPCookieProcessor
from fake_useragent import UserAgent
from http.cookiejar import MozillaCookieJar #  用于保存cookie


# 登录

# 保存cookie文件中
def get_cookie():
    login_url = ""
    headers= {
        "User-Agent": UserAgent().chrome
    }
    from_data = {

    }
    f_data = urlencode(from_data).encode()
    request = Request(login_url, headers=headers, data=f_data)

    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)

    # 无论如何都需要保存. 忽略cookie失效,  或者超时
    cookie_jar.save("cookie.txt", ignore_discard=True, ignore_expires=True)

def use_cookie():
    info_url = ""
    headers = {
        "User-Agent": UserAgent().chrome
    }
    request = Request(info_url, headers=headers)

    cookie_jar = MozillaCookieJar()

    cookie_jar.load("cookie.txt", ignore_discard=True, ignore_expires=True)

    handler = HTTPCookieProcessor(cookie_jar)

    opener = build_opener(handler)

    response = opener.open(request)

    print(response.read().decode())







# 获取cookie从文件中

# 访问页面.