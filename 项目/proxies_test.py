import requests
from fake_useragent import UserAgent



url = "http://httpbin.org/get" # test url


headers = {
    "User-Agent": UserAgent().random
}
proxies = {
    "http": "122.9.101.6:8888"
}

resp = requests.get(url, headers=headers, proxies=proxies)

print(resp.status_code)

print(resp.text)

resp.close()

