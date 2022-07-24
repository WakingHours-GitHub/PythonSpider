"""






"""

from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.error import URLError

url = ""

headers = {
    'User-Agent': UserAgent().chrome
}
try:
    request = Request(url, headers=headers)
    resp = urlopen(request)
    print(resp.read().decode())
except URLError as e:
    if e.args == (): # 通过调试, 看到e中的属性
        print(e.code) # 属性
    else:
        print(e.ags.errorno)

