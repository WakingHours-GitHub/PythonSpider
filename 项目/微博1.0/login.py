import base64
import binascii
import rsa
import requests
from fake_useragent import UserAgent
import time
import re
import json




USER = "15246337585"
PASSWD = ""



sess = requests.session()

headers = {
    'User-Agent': UserAgent().random,
    'Referer': 'https://mail.sina.com.cn/?from=mail', # 需要添加防盗链

}


def pre_login() -> dict:
    url = "https://login.sina.com.cn/sso/prelogin.php"  # note: url not is login really is prelogin
    # 构造预登录时的get参数
    params = {
        "entry": "weibo",
        "callback": "sinaSSOController.preloginCallBack",
        "su": str(base64.b64encode(bytes(USER, encoding='utf-8')), encoding='utf-8'), # 使用base64进行加密. (为什么是base64, 逆向)
        "rsakt": "mod",
        "client": "ssologin.js(v1.4.19)",
        "_": (time.time() * 1000).__str__() # 时间戳 -> string
    }

    # 构造请求
    pre_login = sess.get(url, headers=headers, params=params)

    # pre_login.encoding= 'gb2312'
    # print(pre_login.text) # 有新浪通行证
    # 解析:
    pre_json = re.findall(r"{.*?}", pre_login.text, re.S)[0]
    pre_dict = json.loads(pre_json)

    return pre_dict

# 预登录结束

pre_dict = pre_login() # 返回predict

# 开始登录
# 密码登录.
def encrypt_passwd(passwd, pubkey, servertime, nonce):
    key = rsa.PublicKey(int(pubkey, 16), int('10001', 16)) # 使用rsa算法
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(passwd) # 参数拼接
    passwd = rsa.encrypt(message.encode('utf-8'), key) # 加密.
    return binascii.b2a_hex(passwd) #

def login():
    loginUrl = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)"
    # 模拟登录参数
    params = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'qrcode_flag': 'false',
        'useticket': '1',
        'pagerefer': 'https',
        'vsnf': '1',
        'su': 'MTU2NzU0OTEyODQ=',
        'service': 'miniblog',
        'servertime': pre_dict['servertime'],
        'nonce': pre_dict['nonce'],  # 预登录拿到的东西
        'pwencode': 'rsa2',
        'rsakv': pre_dict['rsakv'],
        'sp': encrypt_passwd(PASSWD, pre_dict['pubkey'], pre_dict['servertime'], pre_dict['nonce']),
        'sr': '1536*864',  # sp就是加密的密码
        'encoding': 'UTF-8',
        # 'prelt': '35',
        'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }
    print(params)
    login_resp = sess.post(loginUrl, headers=headers, params=params)
    login_resp.encoding='gbk'
    print(login_resp.text) #
    # 请求ajax请求, 拿到token参数
    ajax_url = re.findall('https://.*?"', login_resp.text)[-1]
    print(ajax_url)



def main():
    login()
    sess.close()


if __name__ == '__main__':
    main()