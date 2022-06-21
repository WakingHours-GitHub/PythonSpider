# cookies参数的使用
# 只用cookies参数保持会话
# 构建cookies自带你
# 再请求的时候将cookies字典复制给cookies参数
# requests.get(url, cookies)

import requests

# github登录不上去, 所以这里使用, 哔哩哔哩

url = "https://account.bilibili.com/account/home"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
}

# 构建cookie字典
temp = "buvid3=905BF5E6-433D-EFBF-7557-362FCAC50E0355330infoc; CURRENT_FNVAL=976; blackside_state=1; rpdid=|(kuu|mm)~u|0J'uYJJkRYuYm; buvid_fp=905BF5E6-433D-EFBF-7557-362FCAC50E0355330infoc; SESSDATA=b529314e%2C1648798191%2C6a7f5%2Aa1; bili_jct=2bd107f50ebbd7bfe69a7d5a4e92e636; DedeUserID=26537959; DedeUserID__ckMd5=70b0bd7ba36a814f; sid=j5g6c8kk; CURRENT_QUALITY=80; _uuid=F4067729-E0A2-9D6C-3E17-4F89038A9CDE51949infoc; video_page_version=v_old_home_12; fingerprint3=717fbe469452633c0c8a3bcbdb3900f7; buvid_fp_plain=905BF5E6-433D-EFBF-7557-362FCAC50E0355330infoc; innersign=0; fingerprint=0b99c1584f669036f2c8f4bce0f150d4; fingerprint_s=9d5e69e853c36b00c1c620a1a5637116"
# 生成一个字典：
# 旧办法：稳妥方案
cookie_list = temp.split('; ')
cookies = {}
for cookie in cookie_list:
    cookies[cookie.split('=')[0]] = cookie.split('=')[-1] # 一个是key拿左边的值， 一个是value拿右边的值

print(cookies)

# 字典生成式
cookies = {cookie.split('=')[0]: cookie.split('=')[-1] for cookie in cookie_list}

# 使用cookies参数
resp = requests.get(url, headers=headers, cookies=cookies)

print(resp.content.decode())