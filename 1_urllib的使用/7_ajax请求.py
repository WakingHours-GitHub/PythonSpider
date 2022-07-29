"""
ajax请求: 动态页面.
通过请求ajax请求, 动态的请求数据, 然后填入html中
在网络工具: 使用XHR就是过滤ajax请求

例如: 豆瓣排行榜, 动态刷取请求, 数据一点一点的进行添加.



"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote  # 参数解析
from fake_useragent import UserAgent

# 查看网页源代码, 如果没有所需要的数据, 那么大部分情况下, 该数据采用的是动态请求.
# 只要是ajax请求. headers中: X-Requested-With: XMLHttpRequest

"https://movie.douban.com/j/chart/top_list"
# %开头的编码, 也成为url编码, 也称为百分号编码, 是统一资源定位(URL)编码方式.
base_url = "https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}&genres=%E5%89%A7%E6%83%85"
# 如果想要提高效率, 我们可以修改limit的值(MySql的分页), 让其一次返回更多条的数据(通常是json). 但通常不是无限大, 容易造成服务器崩溃, 并且通信时容易丢失.
print(base_url.decode())
i = 0
while True:
    headers = {
        'user-agent': UserAgent().chrome
    }
    # 拼接字符串。不断请求ajax请求。
    url = base_url.format(i * 20)

    request = Request(url, headers=headers)
    response = urlopen(request)
    info = response.read().decode()
    print(info)
    # 判空
    if info == "" or info is None:
        break


    i += 1