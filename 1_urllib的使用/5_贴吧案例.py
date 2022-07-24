from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

CONTENT = "抗压背锅"
PN_PAGE = 3

def getting_page(url):
    headers = {
        'user-agent': UserAgent().random
    }

    # 封装请求头
    request = Request(url, headers=headers)

    # 发送请求
    response = urlopen(request)

    return response.read() # 返回






def save_page(page_bytes, pn):
    with open("./"+CONTENT+"_"+str(pn), 'wb') as f:
        f.write(page_bytes) # 以字节形式写入。


def main() -> None:
    # 准备url：
    raw_url = "https://tieba.baidu.com/f?{}"
    for pn in range(PN_PAGE):
        args = {
            'kw': CONTENT,
            'ie': 'utf-8',
            'pn': pn * 50 # 观察URL页面规律
        }

        url = raw_url.format(urlencode(args))
        page_bytes = getting_page(url)
        # 保存
        save_page(page_bytes, pn) #




if __name__ == '__main__':
    main()